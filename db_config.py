import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

NAME_DB = os.getenv("BD_DATA_BASE")

try:
    mydb = mysql.connector.connect(
        host = os.getenv("BD_HOST"),
        user = os.getenv("BD_ADMIN_USER"),
        password = os.getenv("BD_ADMIN_PASSWORD"),
        database = NAME_DB
    )
    
except mysql.connector.Error as db_error:
    print (f"Erro ao executar o JOIN: {db_error}")
except Exception as e:
    print (f"Erro inesperado: {e}")

mycursor = mydb.cursor()

