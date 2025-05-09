from tabulate import tabulate
from db_config import mycursor, NAME_DB
import os

def list_itens(item: str, table_name: str = None):
    """
    Lista tabelas ou colunas do banco de dados.

    item: 'tables' ou 'columns'
    table_name: nome da tabela (necessário apenas para 'columns')
    """
    try:
        if item.lower() == "tables":
            command = f"SHOW TABLES FROM `{NAME_DB}`"
            params = None
        elif item.lower() == "columns":
            if not table_name:
                raise ValueError("Você precisa fornecer o nome da tabela para visualizar colunas.")
            command = f"SHOW COLUMNS FROM `{table_name}` FROM `{NAME_DB}`"
            params = None
        else:
            raise ValueError("Comando inválido. Use apenas 'tables' ou 'columns'.")

        if params:
            mycursor.execute(command, params)
        else:
            mycursor.execute(command)

        print(f"\n{item.title()} existentes:\n")
        for result in mycursor:
            print(f" - {result[0]}")

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
                
