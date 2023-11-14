import mysql.connector


class Config:
    def __init__(self):
        self.mysql_config = {
            'user': 'root',
            'password': 'B!UEla$agna6988',
            'host': 'localhost',
            'database': 'healthwave'
        }
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="B!UEla$agna6988",
            database="healthwave"
        )

    # connect to database
    def conn_db(self):
        return mysql.connector.connect(**self.mysql_config)

    # create cursor to execute mySQL code
    def conn_cursor(self):
        cursor = self.db.cursor()

        return cursor

    # PRINT TABLE
    def get_table(self, table_name):
        # Connect to the MySQL database
        conn = mysql.connector.connect(**self.mysql_config)
        cursor = conn.cursor()

        # Execute the SELECT query to retrieve the data from the table
        cursor.execute(
            f"SELECT * FROM {table_name};".format(table_name=table_name))
        result = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Return the result of the query
        return result
