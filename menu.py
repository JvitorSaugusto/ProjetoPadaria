from functions import list_itens, select_table, filter_join, filter_table, is_safe_query
from tabelas import create_full_report_xlsx, create_report_xlsx_from_query
from produto import Product
from pdfs import create_full_report_pdf, create_report_pdf_from_query
from db_config import mydb

class Menu:
    def __init__(self, cursor):
        self.cursor = cursor

    def show_main_menu(self):
        while True:
            print('\nSistema da Padaria - Gerenciamento de Banco de Dados')
            print("1 - [Visualizar]")
            print("2 - [Consultar tabela]")
            print("3 - [Área de produtos]")
            print("4 - [Área de relatórios]")
            print("5 - [Salvar alterações]")
            print("0 - [Sair do sistema]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                submenu = View_submenu(self.cursor)
                submenu.show_menu()
                
            elif opcao == "2":
                submenu = Submenu_Query(self.cursor)
                submenu.show_menu()
                
            elif opcao == "3":
                submenu = Submenu_product(self.cursor)
                submenu.show_menu()
                
            elif opcao == "4":
                submenu = Submenu_report(self.cursor)
                submenu.show_menu()
                
            elif opcao == "5":
                save_roll = input("Tem certeza que deseja salvar? s/n").lower()
                if save_roll == "s":
                    mydb.commit()
                    print("Alterações salvas com sucesso")
                else:
                    mydb.rollback()
                    print("Alterações descartadas.")
                break
            
            elif opcao == "0":
                confirm = input("Deseja salvar as alterações antes de sair? (s/n): ").lower()
                if confirm == "s":
                    mydb.commit()
                    print("Alterações salvas com sucesso.")
                else:
                    mydb.rollback()
                    print("Alterações descartadas.")
                print("Encerrando programa...")
                break

# Submenu para visualizar tabelas e colunas
class View_submenu(Menu):
    def show_menu(self):
        while True:
            print("\nVisualizar:")
            print("1 - [Tabelas]")
            print("2 - [Colunas]")
            print("0 - [Voltar]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                try:
                    list_itens("tables")
                except Exception as e:
                    print(f"Erro ao listar tabelas: {e}")
            elif opcao == "2":
                table_name = input("Nome da tabela: ").strip()
                try:
                    list_itens("columns", table_name)
                except Exception as e:
                    print(f"Erro ao listar colunas: {e}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

# Submenu para consultas com SQL dinâmico
class Submenu_Query(Menu):
    def show_menu(self):
        while True:
            print("\nConsultas:")
            print("1 - [Total]")     # SELECT * FROM tabela
            print("2 - [Parcial]")   # SELECT colunas FROM tabela WHERE condição
            print("3 - [JOIN]")      # SELECT com JOIN
            print("0 - [Voltar]")
            opcao = input("Escolha uma opção: ").strip()
            
            try:
                if opcao == "1":
                    table = input("Tabela: ").strip()
                    print(select_table(table))
                elif opcao == "2":
                    table = input("Tabela: ").strip()
                    columns = input("Colunas (separadas por vírgula): ").strip()
                    filter = input("Filtro WHERE: ").strip()
                    print(filter_table(columns, table=table, filter_=filter))
                elif opcao == "3":
                    table = input("Tabela principal: ").strip()
                    join_tabela = input("Tabela a unir: ").strip()
                    columns = input("Colunas (separadas por vírgula): ").strip().split(',')
                    on_cond = input("Condição ON: ").strip()
                    join_type = input("Tipo de JOIN (INNER, LEFT, RIGHT): ").strip()
                    filter = input("Filtro WHERE (opcional): ").strip() or None

                    print(filter_join(
                        *columns, table=table, join_table=join_tabela,
                        on_condition=on_cond, type_join=join_type, filter_=filter
                    ))
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida!")
                    
            except Exception as e:
                print(f"Erro na consulta: {e}")
                    
# Submenu para exportar relatórios de tabelas
class Submenu_report(Menu):
    def show_menu(self):
        while True:
            print("\nGerar relatórios:")
            print("1 - [Gera relatórios com todos os dados de uma tabela]")
            print("2 - [Gera relatórios com consultas e dados personalizados]")
            print("0 - [Voltar]")
            option = input("Escolha uma opção: ").strip()

            if option == "1":
                table = input("De qual Tabela deseja exportar os dados?: ").strip()
                print("Em qual formato deseja exportar?")
                print("1 - [Formato de Planilha]")
                print("2 - [Formato de PDF]")
                option = input("Escolha uma opção: ").strip()
                
                try:
                    if option == "1":
                        create_full_report_xlsx(table)
                        print(f"Dados de {table} exportados com sucesso para XLSX!")
                    elif option == "2":
                        create_full_report_pdf(table)
                        print(f"Dados de {table} exportados com sucesso para PDF!")
                    else:
                        print("Opção inválida")
                except Exception as e:
                    print(f"Erro ao exportar relatório: {e}")
            elif option == "2":
                sql_query = input("Digite sua consulta SQL (somente SELECT): ")
                report_name = input("Digite o nome do seu relatório (opcional)")
                print("Em qual formato deseja exportar?")
                print("1 - [Formato de Planilha]")
                print("2 - [Formato de PDF]")
                option = input("Escolha uma opção: ").strip()
                if option == "1":
                    if is_safe_query(sql_query):
                        create_report_xlsx_from_query(sql_query, report_name)
                    else:
                        print("Consulta potencialmente perigosa! Somente SELECTs simples são permitidos.")
                elif option == "2":
                    if is_safe_query(sql_query):
                        create_report_pdf_from_query(sql_query, report_name)
                    else:
                        print("Consulta potencialmente perigosa! Somente SELECTs simples são permitidos.")

            elif option == "0":
                break
            else:
                print("Opção inválida!")
                
# Submenu específico para CRUD de produtos
class Submenu_product(Menu):
    def show_menu(self):
        while True:
            print("\nGerenciar produtos:")
            print("1 - [Adicionar produto]")
            print("2 - [Remover produto]")
            print("3 - [Atualizar preço]")
            print("4 - [Exportar todos os produtos para...]")
            print("0 - [Voltar]")
            option = input("Escolha uma opção: ").strip()

            if option == "1":
                try:
                    nome = input("Nome do produto: ").strip()
                    descricao = input("Descrição: ").strip()
                    id_tipo = int(input("ID do tipo: "))
                    preco = float(input("Preço unitário: "))
                    produto = Product(nome, descricao, id_tipo, preco)
                    produto.add_product()
                    
                except ValueError:
                    print("Erro: ID_tipo deve ser um número inteiro e preço deve ser um número válido.")
                except Exception as e:
                    print(f"Erro inesperado ao adicionar produto: {e}")

            elif option == "2":
                try:
                    nome = input("Nome do produto para remover: ").strip()
                    Product.remove_product(nome)
                except Exception as e:
                    print(f"Erro ao remover produto: {e}")

            elif option == "3":
                try:
                    nome = input("Nome do produto para atualizar o preço: ").strip()
                    novo_preco = float(input("Novo preço: "))
                    Product.upgrade_price(nome, novo_preco)
                    
                except ValueError:
                    print("Erro: o preço deve ser um número válido.")
                except Exception as e:
                    print(f"Erro ao atualizar preço: {e}")
                    
            elif option == "4":
                print("1 - [Planilha]")
                print("2 - [PDF]")
                option = input("Escolha uma opção: ").strip()
                try:
                    if option == "1":
                        create_full_report_xlsx("produto")
                        print("Dados dos produtos exportados com sucesso para XLSX!")
                    elif option == "2":
                        create_full_report_pdf("produto")
                        print("Dados dos produtos exportados com sucesso para PDF!")
                    else:
                        print("Opção inválida")
                except Exception as e:
                    print(f"Erro ao exportar relatório: {e}")

            elif option == "0":
                break
            else:
                print("Opção inválida!")
