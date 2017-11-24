import sqlite3

class RedeSocial():

    def __init__(self, nome, dataCriacao = [] ,usuarios = [], grupos = []):
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.usuarios = usuarios
        self.grupos = grupos

    def CriarBanco(self, nome):
        conn  = sqlite3.connect(nome + ".db")
        return  conn



