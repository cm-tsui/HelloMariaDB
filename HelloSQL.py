# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
    host="localhost",
    user="pyuser",
    password="pypassword",
    database="test"
)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # Insert method 1
        mySql_insert_query = """INSERT INTO test (test_name) 
                               VALUES 
                               (CONCAT('Method 1 ',NOW())) """
        #cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into test table")
        #new_id = connection.insert_id(); not work
        new_id = cursor.lastrowid

        # Insert method 2
        from datetime import date
        #today = date.today()
        #d1 = today.strftime("%d/%m/%Y")
        from datetime import datetime
        sql = "INSERT INTO test (id, test_name) VALUES (%s, %s)"
        val = (30, "Method 2 " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        cursor.execute(sql, val)
        connection.commit()
        new_id = cursor.lastrowid
        print(cursor.rowcount, "Record inserted successfully into test table")


        # Update
        sql_update_query = "UPDATE test set test_name = CONCAT(test_name,' (Yes)') where id = " + str(new_id)
        print(sql_update_query)
        cursor.execute(sql_update_query)
        connection.commit()
        print("Record Updated successfully ")

        # Select
        sql_select_Query = "SELECT * FROM test"
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("id = ", row[0], )
            print("test_name = ", row[1], "\n")

        # https://pynative.com/python-mysql-delete-data/
        # Delete a record
        sql_Delete_query = "DELETE FROM test WHERE 1"
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
