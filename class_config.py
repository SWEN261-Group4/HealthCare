import mysql.connector
import datetime


class Config:
    def __init__(self):
        self.mysql_config = {
            'user': 'root',
            'password': 'B!UEla$agna6988',  # change depending on your MySQL password to run
            'host': 'localhost',
            'database': 'healthwave'
        }
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="B!UEla$agna6988",  # change depending on your MySQL password to run
            database="healthwave"
        )

    # connect to database
    def conn_db(self):
        return mysql.connector.connect(**self.mysql_config)

    # create cursor to execute mySQL code
    def conn_cursor(self):
        cursor = self.db.cursor()

        return cursor

    # GET ACTIVE MEDICATIONS
    def get_meds(self, table_name, user_id):
        # Connect to the MySQL database
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        # Execute the SELECT query to retrieve the data from the table
        cursor.execute(
            f"SELECT medication, time_1, time_2, time_3 FROM {table_name} WHERE user_id = '{user_id}';".format(table_name=table_name))
        result = cursor.fetchall()

        # Close the database connection
        conn.close()
        # Return the result of the query
        return result

    # GET HEALTH LOGS FOR A USER
    def get_health_logs(self, user_id):
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT * FROM user_health_logger WHERE user_id = '{user_id}';")
        logs = cursor.fetchall()

        conn.close()
        return logs

    # GET SCHEDULE TIMINGS OF DOCTOR
    def get_available_timings(self, doctor_id):
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT date, slot_9am, slot_10am, slot_11am, slot_12pm, slot_1pm, slot_2pm, slot_3pm, slot_4pm, slot_5pm FROM doctor_booking_schedule WHERE doctor_id = '{doctor_id}';")
        result = cursor.fetchone()

        timings = []
        if result:
            date = result[0]
            slots = result[1:]
            time_slots = ['9am-10am', '10am-11am', '11am-12pm', '12pm-1pm',
                          '1pm-2pm', '2pm-3pm', '3pm-4pm', '4pm-5pm', '5pm-6pm']
            for i, slot in enumerate(slots):
                if slot == 'FREE':
                    timings.append({'date': date, 'time': time_slots[i]})
        conn.close()
        return timings

   # MAKE ASSIGNMENT BOOKED ONCE USER HAS BOOKED WITH DOCTOR
    def book_appointment(self, doctor_id, appointment_date, slot_time):
        conn = self.conn_db()
        cursor = conn.cursor()

        # Update the slot status to "BOOKED" in doctor_booking_schedule
        update_query = f"UPDATE doctor_booking_schedule SET {slot_time} = 'BOOKED' WHERE doctor_id = '{doctor_id}' AND date = '{appointment_date}';"
        cursor.execute(update_query)
        conn.commit()

        conn.close()

    # ADD HEALTH LOG
    def add_healthlog(self, user_id, heart_rate, blood_pressure, body_temperature):
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        values = (user_id, heart_rate, blood_pressure,
                  body_temperature, datetime.datetime.now().date())
        sql_code = "INSERT INTO user_health_logger (user_id, heart_rate, blood_pressure, body_temperature, date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql_code, values)
        conn.commit()
        conn.close()
