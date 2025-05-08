import mysql.connector
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()

try:
    mydb = mysql.connector.connect(
        host = os.getenv("BD_HOST"),
        user = os.getenv("BD_ADMIN_USER"),
        password = os.getenv("BD_ADMIN_PASSWORD"),
        database = "projeto_padaria_t"
    )
    
except Exception as e:
    print(f"Erro: {e}") 

mycursor = mydb.cursor()
