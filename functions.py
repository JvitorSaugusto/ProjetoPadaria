from tabulate import tabulate
from db_config import mycursor, NAME_DB
import mysql.connector
import os

# Função que lista todas as tabelas do BD ou colunas de uma tabela específica
def list_itens(item: str, table_name: str = None):
    """
    Lista tabelas ou colunas do banco de dados.

    item: 'tables' ou 'columns'
    table_name: nome da tabela (necessário apenas para 'columns')
    """
    try:
        if item.lower() == "tables":
            command = f"SHOW TABLES FROM `{NAME_DB}`"
            mycursor.execute(command)

        elif item.lower() == "columns":
            if not table_name:
                raise ValueError("Você precisa fornecer o nome da tabela para visualizar colunas.")
            command = f"SHOW COLUMNS FROM `{table_name}` FROM `{NAME_DB}`"
            mycursor.execute(command)

        else:
            raise ValueError("Comando inválido. Use apenas 'tables' ou 'columns'.")
        
        if item.lower() == "tables":
            print("\nTodas as tabelas existentes no banco de dados:\n")
        elif item.lower() == "columns":
            print(f"\nColunas da tabela '{table_name}':\n")
        for result in mycursor:
            print(f" - {result[0]}")

    except mysql.connector.Error as db_error:
        return f"Erro de banco de dados: {db_error}"
    except ValueError as ve:
        return f"Erro de validação: {ve}"
    except TypeError as te:
        return f"Erro de tipo: {te}"
    except Exception as e:
        return f"Erro inesperado: {e}"


def select_table(table):
    print("\nAqui estão os dados atuais de sua tabela: \n")
    try:
        mycursor.execute(f"SELECT * FROM {table}")
        all_data = mycursor.fetchall()
        header_name = [column[0] for column in mycursor.description]
        return tabulate(all_data, headers=header_name, tablefmt="grid")
    
    except mysql.connector.Error as db_error:
        return f"Erro de banco de dados: {db_error}"
    except Exception as e:
        return f"Erro inesperado: {e}"


def filter_table(*items, table, filter_=None):
    columns = ", ".join(items)
    sql = f"SELECT {columns} FROM {table}"
    if filter_:
        sql += f" WHERE {filter_}"
    try:
        mycursor.execute(sql)
        data = mycursor.fetchall()
        headers = [col[0] for col in mycursor.description]
        return tabulate(data, headers=headers, tablefmt="grid")
    
    except mysql.connector.Error as db_error:
        return f"Erro de banco de dados: {db_error}"
    except Exception as e:
        return f"Erro inesperado: {e}"


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
    
    except mysql.connector.Error as db_error:
        return f"Erro ao executar o JOIN: {db_error}"
    except Exception as e:
        return f"Erro inesperado: {e}"

def clean_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Função para validar se uma string contém apenas letras (sem números)
def verify_is_str(value: str):
    
    while True:
        if any(char.isdigit() for char in value):
            value = input('Valor inválido, digite novamente: ')
        else:
            return value

def is_safe_query(sql_query: str) -> bool:
    """
    Verifica se a query SQL é segura para execução (somente SELECT).
    Bloqueia comandos perigosos como INSERT, UPDATE, DELETE, etc.
    """
    sql = sql_query.strip().lower()
    
    # Lista de palavras proibidas
    keywords_block = ["insert", "update", "delete", "drop", "alter", "create", "--", ";"]
    
    return (
        sql.startswith("select")
        and not any(keyword in sql for keyword in keywords_block)
    )