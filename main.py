import mysql.connector
from dotenv import load_dotenv
import os

try:
    def connect_db(schema):
        my_db = mysql.connector.connect(
            host = os.getenv("BD_HOST"),
            user = os.getenv("BD_ADMIN_USER"),
            password = os.getenv("BD_ADMIN_PASSWORD"),
            database=schema
        )

except:
        print('Fatal Error')
        

def list_db_schemas():
    mycursor = my_db.cursor()
    mycursor.execute("SHOW DATABASES")

    for schema in mycursor:
     print(schema)
     
list_db_schemas()

