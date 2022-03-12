import os
from dotenv import load_dotenv
import mysql.connector

# VENV Importing
load_dotenv()

HST = os.getenv('HST')
PRT = os.getenv('PRT')
USR = os.getenv('USR')
PSS = os.getenv('PSS')
DBE = os.getenv('DBE')


# Update Database
def insert_data(email, password, branch, subject):
    mydb = mysql.connector.connect(
        host=HST,
        port=PRT,
        user=USR,
        password=PSS,
        database=DBE
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s);", (email, password, branch, subject))
    mydb.commit()
    mydb.close()