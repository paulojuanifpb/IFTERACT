import datetime

class RedeSocial():

    def __init__(self, nome, descricao, dataCriacao = datetime.date.today() ,usuarios = [], grupos = []):
        self.nome = nome
        self.descricao = descricao
        self.dataCriacao = dataCriacao
        self.usuarios = usuarios
        self.grupos = grupos




