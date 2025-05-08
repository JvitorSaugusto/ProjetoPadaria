from tabulate import tabulate
from db_config import mycursor, NAME_DB
import os

def list_itens(item: str, extra=""):
    """
    item: comando após SHOW (ex: 'tables', 'columns')
    extra: informações adicionais (ex: 'FROM cliente' para colunas)
    """
    try:
        if item.lower() == "tables":
            command = "SHOW TABLES FROM %s"
            params = (NAME_DB,)
        elif item.lower() == "columns":
            # extra deve ser algo como "FROM nome_tabela"
            command = "SHOW COLUMNS %s"
            params = (extra,) 
        else:
            command = f"SHOW {item.upper()} {extra}".strip()

        mycursor.execute(command, params)
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
    print("\nAqui estão os dados atuais de sua tabela: \n")
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

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def verify_is_str(value:str):
    #checks if string contains no digits
    while True:
            if any(char.isdigit() for char in value):
                value = input('Valor invalido, digite novamente: ')
            else:
                return value
                
