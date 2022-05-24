import mysql.connector
from mysql.connector import Error

try:
    db = '*****************'
    
    mydb = mysql.connector.connect(
        host='*****************-mysql.services.clever-cloud.com',
        port=3306,
        user='*****************',
        password='*****************',
        database=db
    )

    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print(f"Connected to MySQL Server version {db_Info}")
        cursor = mydb.cursor()
        cursor.execute("select database();")
        dbname = cursor.fetchone()
        print(f"You're connected to database: {db}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")