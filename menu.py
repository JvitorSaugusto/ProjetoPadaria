from functions import list_itens, select_table, filter_join, filter_table, is_safe_query, clean_terminal
from tabelas import create_full_report_xlsx, create_report_xlsx_from_query
from produto import Product
from pdfs import create_full_report_pdf, create_report_pdf_from_query
from db_config import mydb

class Menu:
    def __init__(self, cursor):
        self.cursor = cursor

    def show_main_menu(self):
        while True:
            clean_terminal()
            print('\n=== Sistema da Padaria - Gerenciamento de Banco de Dados ===')
            print("1 - [Visualizar estrutura do banco]")
            print("2 - [Consultar dados das tabelas]")
            print("3 - [Gerenciar produtos]")
            print("4 - [Gerar relatórios]")
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
                save_roll = input("Tem certeza que deseja salvar? (s/n): ").lower()
                if save_roll == "s":
                    mydb.commit()
                    print("✅ Alterações salvas com sucesso.")
                else:
                    mydb.rollback()
                    print("⚠️ Alterações descartadas.")
                input("\nPressione Enter para continuar...")
                break
            
            elif opcao == "0":
                confirm = input("Deseja salvar as alterações antes de sair? (s/n): ").lower()
                if confirm == "s":
                    mydb.commit()
                    print("✅ Alterações salvas com sucesso.")
                else:
                    mydb.rollback()
                    print("⚠️ Alterações descartadas.")
                print("Encerrando programa...")
                input("\nPressione Enter para continuar...")
                break

class View_submenu(Menu):
    def show_menu(self):
        while True:
            clean_terminal()
            print("\n--- Visualização da Estrutura do Banco de Dados ---")
            print("1 - [Listar todas as tabelas]")
            print("2 - [Listar colunas de uma tabela]")
            print("0 - [Voltar ao menu principal]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                try:
                    list_itens("tables")
                except Exception as e:
                    print(f"Erro ao listar tabelas: {e}")
                input("\nPressione Enter para continuar...")
            elif opcao == "2":
                table_name = input("Digite o nome da tabela: ").strip()
                try:
                    list_itens("columns", table_name)
                except Exception as e:
                    print(f"Erro ao listar colunas: {e}")
                input("\nPressione Enter para continuar...")
            elif opcao == "0":
                break
            else:
                print("⚠️ Opção inválida!")
                input("\nPressione Enter para continuar...")

class Submenu_Query(Menu):
    def show_menu(self):
        while True:
            clean_terminal()
            print("\n--- Consultas SQL ---")
            print("1 - [Exibir todos os dados de uma tabela]")
            print("2 - [Consulta personalizada com filtros]")
            print("3 - [Consulta com JOIN entre tabelas]")
            print("0 - [Voltar ao menu principal]")
            opcao = input("Escolha uma opção: ").strip()
            
            try:
                if opcao == "1":
                    table = input("Digite o nome da tabela: ").strip()
                    print(select_table(table))
                elif opcao == "2":
                    table = input("Tabela: ").strip()
                    columns = input("Colunas (separadas por vírgula): ").strip()
                    filter = input("Filtro WHERE: ").strip()
                    print(filter_table(columns, table=table, filter_=filter))
                elif opcao == "3":
                    table = input("Tabela principal: ").strip()
                    join_tabela = input("Tabela a ser unida: ").strip()
                    columns = input("Colunas (separadas por vírgula): ").strip().split(',')
                    on_cond = input("Condição ON (ex: t1.id = t2.id_tabela): ").strip()
                    join_type = input("Tipo de JOIN (INNER, LEFT, RIGHT): ").strip()
                    filter = input("Filtro WHERE (opcional): ").strip() or None

                    print(filter_join(
                        *columns, table=table, join_table=join_tabela,
                        on_condition=on_cond, type_join=join_type, filter_=filter
                    ))
                elif opcao == "0":
                    break
                else:
                    print("⚠️ Opção inválida!")
            except Exception as e:
                print(f"Erro na consulta: {e}")
            input("\nPressione Enter para continuar...")

class Submenu_report(Menu):
    def show_menu(self):
        while True:
            clean_terminal()
            print("\n--- Geração de Relatórios ---")
            print("1 - [Exportar todos os dados de uma tabela]")
            print("2 - [Exportar dados de uma consulta personalizada]")
            print("0 - [Voltar ao menu principal]")
            option = input("Escolha uma opção: ").strip()

            if option == "1":
                table = input("Digite o nome da tabela: ").strip()
                print("Escolha o formato de exportação:")
                print("1 - [Planilha XLSX]")
                print("2 - [Arquivo PDF]")
                option = input("Escolha uma opção: ").strip()
                
                try:
                    if option == "1":
                        create_full_report_xlsx(table)
                        print(f"✅ Dados da tabela '{table}' exportados com sucesso para XLSX!")
                    elif option == "2":
                        create_full_report_pdf(table)
                        print(f"✅ Dados da tabela '{table}' exportados com sucesso para PDF!")
                    else:
                        print("⚠️ Opção inválida.")
                except Exception as e:
                    print(f"Erro ao exportar relatório: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "2":
                sql_query = input("Digite sua consulta SQL (somente SELECT): ").strip()
                report_name = input("Nome do relatório (opcional): ").strip()
                print("Escolha o formato de exportação:")
                print("1 - [Planilha XLSX]")
                print("2 - [Arquivo PDF]")
                option = input("Escolha uma opção: ").strip()
                
                try:
                    if is_safe_query(sql_query):
                        if option == "1":
                            create_report_xlsx_from_query(sql_query, report_name)
                            print("✅ Relatório exportado com sucesso em XLSX!")
                        elif option == "2":
                            create_report_pdf_from_query(sql_query, report_name)
                            print("✅ Relatório exportado com sucesso em PDF!")
                        else:
                            print("⚠️ Opção inválida.")
                    else:
                        print("❌ Consulta potencialmente perigosa! Apenas SELECTs simples são permitidos.")
                except Exception as e:
                    print(f"Erro ao gerar relatório: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "0":
                break
            else:
                print("⚠️ Opção inválida!")
                input("\nPressione Enter para continuar...")

class Submenu_product(Menu):
    def show_menu(self):
        while True:
            clean_terminal()
            print("\n--- Gerenciamento de Produtos ---")
            print("1 - [Adicionar novo produto]")
            print("2 - [Remover produto existente]")
            print("3 - [Atualizar preço do produto]")
            print("4 - [Exportar todos os produtos]")
            print("0 - [Voltar ao menu principal]")
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
                    print("❌ ID do tipo deve ser inteiro e preço deve ser um número válido.")
                except Exception as e:
                    print(f"Erro inesperado ao adicionar produto: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "2":
                try:
                    nome = input("Nome do produto a ser removido: ").strip()
                    Product.remove_product(nome)
                except Exception as e:
                    print(f"Erro ao remover produto: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "3":
                try:
                    nome = input("Nome do produto: ").strip()
                    novo_preco = float(input("Novo preço: "))
                    Product.upgrade_price(nome, novo_preco)
                except ValueError:
                    print("❌ O preço deve ser um número válido.")
                except Exception as e:
                    print(f"Erro ao atualizar preço: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "4":
                print("Escolha o formato de exportação:")
                print("1 - [Planilha XLSX]")
                print("2 - [Arquivo PDF]")
                option = input("Escolha uma opção: ").strip()
                try:
                    if option == "1":
                        create_full_report_xlsx("produto")
                        print("✅ Produtos exportados com sucesso para XLSX!")
                    elif option == "2":
                        create_full_report_pdf("produto")
                        print("✅ Produtos exportados com sucesso para PDF!")
                    else:
                        print("⚠️ Opção inválida.")
                except Exception as e:
                    print(f"Erro ao exportar produtos: {e}")
                input("\nPressione Enter para continuar...")

            elif option == "0":
                break
            else:
                print("⚠️ Opção inválida!")
                input("\nPressione Enter para continuar...")
