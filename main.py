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
        database = "projeto padaria"
    )
    
except Exception as e:
    print(f"Erro: {e}") 

mycursor = mydb.cursor()

def list_itens(item: str, extra=""):
    command = f"SHOW {item.upper()} {extra}".strip()
    """
    item: command after SHOW (example: 'databases', 'tables', 'columns')
    extra: infos extras (ex: 'FROM cliente' to show columns)
    """
    try:
        mycursor.execute(command)
        print(f"\n{item.title()} existentes:\n")
        
        if item.lower() == "columns":
            for result in mycursor:
                print(f" - {result[0]}")
        
        else:
            for (result,) in mycursor:
                print(f" - {result}")
                
    except Exception as e:
        print(f"Erro: {e}") 
        
def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    all_data = mycursor.fetchall()
    header_name = [column[0] for column in mycursor.description]
    return tabulate(all_data, headers=header_name, tablefmt="grid")
       
       

            
list_itens("columns", "FROM cliente")

#list_db_schemas()
#show_tables()
#print(show_data_table('cliente'))