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
          
print(filter_table(("CPF, NOME"), table=("cliente"), filter_=("NOME LIKE 'A%'")))

#list_itens("columns", "FROM cliente")

#list_db_schemas()
#show_tables()
#print(show_data_table('cliente'))

while True:
    print('Programa de gerenciamento de DB iniciado')
    menu = input(f"Escolha uma das opções: 1 - [visualizar] 2 -[consultar tabela] 0 - [sair do sistema]")
    
    if menu == "1":
        submenu_show = input(f"O que você deseja visualizar? todos os(as): 1 - [Banco de dados instalados] 2 - [tabelas existentes DB] 3 - [colunas de uma tabela] 0 - [voltar]")
        
        #submenu 1
        if submenu_show == "1":
            list_itens("databases")
        elif submenu_show == "2":
            db_name = input("De qual banco deseja ver as tabelas? ").strip()
            list_itens("tables", f"FROM {db_name}")
        elif submenu_show == "3":
            table_name = input("De qual tabela deseja ver as colunas? ").strip()
            list_itens("columns", f"FROM {table_name}")
        elif submenu_show == "0":
            continue
        else:
            print("Opção inválida!")
            
    elif menu == "2":
        submenu_select = input(f"Qual o tipo da consulta? 1 - [total] 2 - [parcial] 3 - [com join] 0 - [voltar]") 
        #submenu 2
        if submenu_select == "1":
            table_name = input("Qual tabela quer realizar a consulta total? ").strip()
            
            select_table(f"{table_name}")
            
        elif submenu_select == "2":
            table_name = input("Qual tabela quer realizar a consulta parcial? ").strip()
            columns_name = input(f"Quais colunas da tabela {table_name}?").strip()
            where_name = input(f"Qual filtro deseja aplicar?").strip()
            
            filter_table(columns_name, table_name, where_name)
            
        elif submenu_select == "3":

            table = input("Qual a tabela principal? ").strip()
            join_table = input("Qual tabela será unida? ").strip()
            
            # exibir as colunas das tabelas selecionadas, talvez caiba um thread aqui
            
            columns = input("Quais colunas deseja selecionar (separadas por vírgula)? ").strip().split(',')
            on_condition = input("Qual a condição de JOIN (ex: tabela1.id = tabela2.id_tabela1)? ").strip()
            join_type = input("Qual tipo de JOIN (INNER, LEFT, RIGHT, FULL)? ").strip().upper()
            where_filter = input("Qual filtro deseja aplicar (deixe em branco se não quiser)? ").strip() or None

            filter_join(
                *columns, table=table, join_table=join_table, on_condition=on_condition, type_join=join_type, filter_=where_filter
)

        elif submenu_select == "0":
            continue
        
        else:
            print("Opção inválida!")

    elif menu == "0":
        print("Encerrando programa...")
        break
    