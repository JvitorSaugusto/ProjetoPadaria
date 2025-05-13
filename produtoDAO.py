from db_config import mycursor, NAME_DB
from functions import select_table  
from produto import Produto

class ProdutoDAO():
    @staticmethod
    def add_product(produto: Produto):
        sql = "INSERT INTO produto (nome, descricao, id_tipo_prod, preco_unidade) VALUES (%s, %s, %s, %s)"
        values = (produto.nome, produto.descricao, produto.id_tipo_prod, produto.preco_unidade)
        mycursor.execute(sql, values)
        print(select_table("produto"))
    @staticmethod
    def remove_product(nome: str, mycursor):
        sql = "DELETE FROM produto WHERE nome = (%s)"
        mycursor.execute(sql, (nome,))
        print(select_table("produto"))
    @staticmethod        
    def update_price(nome: str, preco_unidade: float, mycursor ):
        sql = "UPDATE produto SET preco_unidade = %s WHERE nome = %s"
        values = (preco_unidade, nome)
        mycursor.execute(sql, values) 
        print(f"Preço do produto {nome} atualizado para {preco_unidade}")