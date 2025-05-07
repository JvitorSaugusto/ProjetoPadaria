import mysql.connector
from dotenv import load_dotenv
import os
from tabulate import tabulate
from db_config import mycursor
load_dotenv()

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
       

def filter_table(*items, table, filter_=None):
    columns = ", ".join(items)
    sql = f"SELECT {columns} FROM {table}"
    if filter_:
        sql += f" WHERE {filter_}"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    headers = [col[0] for col in mycursor.description]
    return tabulate(data, headers=headers, tablefmt="grid")
            
  
  
def filter_join(*items, table, join_table, on_condition, type_join, filter_=None):
    columns = ", ".join(items)
    
    sql = f"SELECT {columns} FROM {table} {type_join.upper()} JOIN {join_table} ON {on_condition}"
    
    
    if filter_:
        sql += f" WHERE {filter_}"
        
    try:
        mycursor.execute(sql)
        data = mycursor.fetchall()
        headers = [col[0] for col in mycursor.description]
        return tabulate(data, headers=headers, tablefmt="grid")

    except Exception as e:
        return f"Erro ao executar o JOIN: {e}"
    

if __name__ == "__main__":
    