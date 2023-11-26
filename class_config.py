import mysql.connector
import datetime


class Config:
    def __init__(self):
        self.mysql_config = {
            'user': 'root',
            'password': 'password',  # change depending on your MySQL password to run
            'host': 'localhost',
            'database': 'healthwave2'  # change to the name of ur database
        }
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # change depending on your MySQL password to run
            database="healthwave2"  # change to the name of ur database
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
            f"SELECT date, slot_9, slot_10, slot_11, slot_12, slot_13, slot_14, slot_15, slot_16, slot_17 FROM doctor_booking_schedule WHERE doctor_id = '{doctor_id}';")
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
                elif slot == 'BOOKED':
                    timings.append(
                        {'date': date, 'time': f'{time_slots[i]} BOOKED'})
        conn.close()
        return timings

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

    # ADD APPOINTMENT
    def add_appointment(self, appointment_id, user_id, appointment_date, slot_time, doctor_full_name, doctor_id):
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        values = (appointment_id, user_id, appointment_date,
                  slot_time, doctor_full_name, doctor_id)
        sql_code = "INSERT INTO user_appointments (appointment_id, user_id, date, time, doctor_full_name, doctor_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_code, values)
        conn.commit()
        conn.close()

    # GET ACTIVE APPOINTMENTS
    def get_appointments(self, user_id):
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT * FROM user_appointments WHERE user_id = '{user_id}' ORDER BY date;")
        appointments = cursor.fetchall()

        conn.close()
        return appointments

   # MAKE APPOINTMENT BOOKED ONCE USER HAS BOOKED WITH DOCTOR

    def book_appointment(self, doctor_id, appointment_date, chosen_time):
        conn = self.conn_db()
        cursor = conn.cursor()

        # Assuming chosen_time holds '2:00 PM' as an example
        hour = chosen_time.split(':')[0]

        # Construct the column name based on the normalized chosen time
        slot = f"slot_{hour}"

        # Check if the date for the doctor exists in the doctor_booking_schedule
        check_query = "SELECT COUNT(*) FROM doctor_booking_schedule WHERE doctor_id = %s AND date = %s"
        cursor.execute(check_query, (doctor_id, appointment_date))
        row_count = cursor.fetchone()[0]

        if row_count == 0:
            # If the row doesn't exist, insert a new row for that date and doctor ID
            insert_query = "INSERT INTO doctor_booking_schedule (doctor_id, date, slot_9, slot_10, slot_11, slot_12, slot_13, slot_14, slot_15, slot_16, slot_17) VALUES (%s, %s, 'FREE','FREE','FREE','FREE','FREE','FREE','FREE','FREE','FREE')"
            cursor.execute(insert_query, (doctor_id, appointment_date))
            conn.commit()

        # Update the slot status to "BOOKED" in doctor_booking_schedule using parameterized query
        update_query = f"UPDATE doctor_booking_schedule SET `{slot}` = 'BOOKED' WHERE doctor_id = %s AND date = %s"
        cursor.execute(update_query, (doctor_id, appointment_date))
        conn.commit()

        conn.close()
