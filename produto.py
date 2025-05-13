from functions import verify_is_str

class Produto():
    def __init__(self, nome:str, descricao:str, id_tipo_prod:int, preco_unidade:int):
        verify_is_str(self.nome)
        self.nome=nome
        self.descricao=descricao
        self.id_tipo_prod=id_tipo_prod
        self.preco_unidade=preco_unidade