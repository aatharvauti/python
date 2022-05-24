import os
from dotenv import load_dotenv
import mysql.connector

print("Atharva Auti Roll No. 1\n")

# VENV Importing
load_dotenv()

HST = os.getenv('HST')
PRT = os.getenv('PRT')
USR = os.getenv('USR')
PSS = os.getenv('PSS')
DBE = os.getenv('DBE')

# Connect
mydb = mysql.connector.connect(
    host=HST,
    port=PRT,
    user=USR,
    password=PSS,
    database=DBE
)
mycursor = mydb.cursor()

# Create
def create_table(table_name, attr1, attr2, attr3):
    query = f"CREATE TABLE {table_name} ({attr1}, {attr2}, {attr3});"
    mycursor.execute(query)
    print("Executed: ", query)
    mydb.commit()


# Read 
def read_all(table_name):
    query = f"SELECT * FROM {table_name};"
    mycursor.execute(query)
    print("Executed: ", query)
    records = mycursor.fetchall()
    print("Records:")
    for row in records:
        print(f"\nPerson [{row}]: ")
        print("ID: ", row[0])
        print("NAME: ", row[1])
        print("PHONE: ", row[2])


# Update
def insert_data(table_name, attr1, attr2, attr3):
    query = f"INSERT INTO {table_name} VALUES (\"{attr1}\", \"{attr2}\", \"{attr3}\");"
    mycursor.execute(query)
    print("Executed: ", query)
    mydb.commit()


# Delete
def delete_data(table_name, condition):
    query = f"DELETE FROM {table_name} WHERE {condition};"
    mycursor.execute(query)
    print("Executed: ", query)
    mydb.commit()


create_table("heckers", "id int", "name varchar(25)", "phone varchar(10)")

insert_data("heckers", "1", "Sakshi", "2344332255")
insert_data("heckers", "2", "Meet", "4242424242")
insert_data("heckers", "3", "XYZ", "0000000000")

read_all("heckers")

delete_data("heckers", "id = 3")

read_all("heckers")
