from db_config import mycursor, NAME_DB
from functions import verify_is_str, select_table

class Produto():
    def __init__(self, nome:str, descricao:str, id_tipo_prod:int, preco_unidade:int):
        self.nome=nome
        self.descricao=descricao
        self.id_tipo_prod=id_tipo_prod
        self.preco_unidade=preco_unidade
    
    def add_product(self, mycursor):
        sql = "INSERT INTO produto (nome, descricao, id_tipo_prod, preco_unidade) VALUES (%s, %s, %s, %s)"
        values = (self.nome, self.descricao, self.id_tipo_prod, self.preco_unidade)
        verify_is_str(self.nome)
        mycursor.execute(sql, values)
        print(select_table("produto"))

    def remove_product(self, mycursor):
        sql = "DELETE FROM produto WHERE nome = (%s)"
        value = (self.nome,)
        verify_is_str(self.nome) 
        mycursor.execute(sql, value)
        print(select_table("produto"))
        
produto1 = Produto("pipoca doce", "Uma pipoca deliciosa, com muito caramelo", 2, 11)
#produto1.add_product(mycursor)
#produto1.remove_product(mycursor)

