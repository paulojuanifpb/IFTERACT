import sqlite3


def criarTabelaUsuario(conn):
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE tb_Usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(70) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                nascimento DATE,
                profissao VARCHAR(50),
                genero VARCHAR(10),
                publico BOOLEAN default FALSE,
                senha VARCHAR(30) NOT NULL
             );

        """)



class Usuario():
    def __init__(self, nome, email, nascimento, profissao, genero, publico, senha):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento
        self.profissao = profissao
        self.genero = genero
        self.publico = publico
        self.senha = senha

    def __str__(self):
        return self.nome + "  " + self.email

def listarUsuarios(conn):

    usuarios = []
    cursor = conn.cursor()
    cursor.execute("""
        Select * From tb_Usuario;
        """)

    for linha in cursor.fetchall():
        nome = linha[1]
        email = linha[2]
        nascimento = linha[3]
        profissao = linha[4]
        genero = linha[5]
        publico = linha[6]
        senha = linha[7]
        usuario = Usuario(nome, email, nascimento, profissao, genero, publico, senha)
        usuarios.append(usuario)
    return usuarios


#conn.close()
