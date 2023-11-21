import mysql.connector


class Config:
    def __init__(self):
        self.mysql_config = {
            'user': 'root',
            'password': "password",  # change depending on your MySQL password to run
            'host': 'localhost',
            'database': 'healthwave'
        }
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # change depending on your MySQL password to run
            database="healthwave"
        )

    # connect to database
    def conn_db(self):
        return mysql.connector.connect(**self.mysql_config)

    # create cursor to execute mySQL code
    def conn_cursor(self):
        cursor = self.db.cursor()

        return cursor

    # SHOW ACTIVE MEDICATIONS
    def get_meds(self, table_name, user_id):
        # Connect to the MySQL database
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        # Execute the SELECT query to retrieve the data from the table
        cursor.execute(
            f"SELECT medication_1, medication_2, medication_3, medication_4, medication_5 FROM {table_name} WHERE user_id = '{user_id}';".format(table_name=table_name))
        result = cursor.fetchall()

        # Close the database connection
        conn.close()
        # Return the result of the query
        return result
