from functions import list_itens, select_table, filter_join, filter_table, limpar_terminal
from tabelas import criar_relatorio_completo
from db_config import NAME_DB
from produto import Produto
from pdfs import create_full_report_pdf
from produtoDAO import ProdutoDAO
class Menu:
    def __init__(self, cursor):
        self.cursor = cursor

    def exibir_menu_principal(self):
        while True:
            print('\nSistema da Padaria - Gerenciamento de Banco de Dados')
            print("1 - [Visualizar]")
            print("2 - [Consultar tabela]")
            print("0 - [Sair do sistema]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                submenu = SubmenuVisualizar(self.cursor)
                submenu.exibir_menu()
            elif opcao == "2":
                submenu = SubmenuConsulta(self.cursor)
                submenu.exibir_menu()
            elif opcao == "0":
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida!")

class SubmenuVisualizar(Menu):
    def exibir_menu(self):
        while True:
            print("\nVisualizar:")
            print("1 - [Tabelas]")
            print("2 - [Colunas]")
            print("0 - [Voltar]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                list_itens("tables")
            elif opcao == "2":
                table_name = input("Nome da tabela: ").strip()
                list_itens("columns", table_name)
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

class SubmenuConsulta(Menu):
    def exibir_menu(self):
        while True:
            print("\nConsultas:")
            print("1 - [Total]")
            print("2 - [Parcial]")
            print("3 - [JOIN]")
            print("0 - [Voltar]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                tabela = input("Tabela: ").strip()
                print(select_table(tabela))
            elif opcao == "2":
                tabela = input("Tabela: ").strip()
                colunas = input("Colunas (separadas por vírgula): ").strip()
                filtro = input("Filtro WHERE: ").strip()
                print(filter_table(colunas, table=tabela, filter_=filtro))
            elif opcao == "3":
                tabela = input("Tabela principal: ").strip()
                join_tabela = input("Tabela a unir: ").strip()
                colunas = input("Colunas (separadas por vírgula): ").strip().split(',')
                on_cond = input("Condição ON: ").strip()
                tipo_join = input("Tipo de JOIN (INNER, LEFT, RIGHT): ").strip()
                filtro = input("Filtro WHERE (opcional): ").strip() or None

                print(filter_join(
                    *colunas, table=tabela, join_table=join_tabela,
                    on_condition=on_cond, type_join=tipo_join, filter_=filtro
                ))
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
        
class Submenu_produto(Menu):
    def exibir_menu(self):
        while True:
            print("\nGerenciar produtos:")
            print("1 - [Adicionar]")
            print("2 - [Remover]")
            print("3 - [Atualizar preço]")
            print("4 - [Exportar para...]")
            print("0 - [Voltar]")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                nome = input("Nome do produto: ").strip()
                descricao = input("Descrição: ").strip()
                id_tipo = int(input("ID do tipo: "))
                preco = float(input("Preço unitário: "))
                produto = Produto(nome, descricao, id_tipo, preco)
                ProdutoDAO.add_product(produto, self.cursor)
            elif opcao == "2":
                nome = input("Nome do produto para remover: ").strip()
                ProdutoDAO.remove_product(produto, self.cursor)
            elif opcao == "3":
                nome = input("Nome do produto para atualizar o preço: ").strip()
                novo_preco = float(input("Novo preço: "))
                ProdutoDAO.update_price(nome, novo_preco, self.cursor)
            elif opcao == "4":
                print("1 - [Planilha]")
                print("2 - [PDF]")
                opcao = input("Escolha uma opção: ").strip()
                if opcao == 1:
                    criar_relatorio_completo("produto")
                elif opcao == 2:
                    create_full_report_pdf("produto")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
