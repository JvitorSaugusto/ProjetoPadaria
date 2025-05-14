from db_config import mycursor
from functions import verify_is_str, select_table
import mysql.connector

class Produto:
    def __init__(self, nome: str, descricao: str, id_tipo_prod: int, preco_unidade: float):
        self.nome = verify_is_str(nome)
        self.descricao = descricao
        self.id_tipo_prod = id_tipo_prod
        self.preco_unidade = preco_unidade

    def adicionar(self):
        sql = "INSERT INTO produto (nome, descricao, id_tipo_prod, preco_unidade) VALUES (%s, %s, %s, %s)"
        valores = (self.nome, self.descricao, self.id_tipo_prod, self.preco_unidade)
        try:
            mycursor.execute(sql, valores)
            print(select_table("produto"))
            
        except mysql.connector.Error as db_error:
            return f"Erro ao executar o JOIN: {db_error}"
        except Exception as e:
            return f"Erro inesperado: {e}"
        
    def remover(nome: str):
        sql = "DELETE FROM produto WHERE nome = %s"
        try:
            mycursor.execute(sql, (nome,))
            print(select_table("produto"))
            
        except mysql.connector.Error as db_error:
            return f"Erro ao executar o JOIN: {db_error}"
        except Exception as e:
            return f"Erro inesperado: {e}"

    def atualizar_preco(nome: str, novo_preco: float):
        sql = "UPDATE produto SET preco_unidade = %s WHERE nome = %s"
        try:
            mycursor.execute(sql, (novo_preco, nome))
            print(f"Preço do produto '{nome}' atualizado para {novo_preco}")
            
        except mysql.connector.Error as db_error:
            return f"Erro ao executar o JOIN: {db_error}"
        except Exception as e:
            return f"Erro inesperado: {e}"