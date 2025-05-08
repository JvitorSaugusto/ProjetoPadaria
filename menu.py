from functions import list_itens, select_table, filter_join, filter_table, limpar_terminal

class Menu:
    def __init__(self, cursor):
        self.cursor = cursor

    def exibir_menu_principal(self):
        while True:

            print('Programa de gerenciamento de DB iniciado')
            opcao = input("Escolha uma das opções: 1 - [visualizar] 2 - [consultar tabela] 0 - [sair do sistema]: ").strip()
            
            if opcao == "1":
                self.exibir_menu_visualizar()
            elif opcao == "2":
                self.exibir_menu_consultas()
            elif opcao == "0":
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida!")
    def exibir_menu_visualizar(self):
        while True:
            
            opcao = input("Visualizar: 1 - [bancos] 2 - [tabelas] 3 - [colunas] 0 - [voltar]: ").strip()
            if opcao == "1":
                list_itens("databases")
            elif opcao == "2":
                nome_db = input("Nome do banco: ").strip()
                list_itens("tables", f"FROM {nome_db}")
            elif opcao == "3":
                nome_tabela = input("Nome da tabela: ").strip()
                list_itens("columns", f"FROM {nome_tabela}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def exibir_menu_consultas(self):
        while True:
            
            opcao = input("Consulta: 1 - [total] 2 - [parcial] 3 - [join] 0 - [voltar]: ").strip()
            if opcao == "1":
                tabela = input("Tabela para SELECT total: ").strip()
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
                on_cond = input("Condição de união (ON): ").strip()
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