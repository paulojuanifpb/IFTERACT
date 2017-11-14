import sqlite3

# CONEXÃO
conn = sqlite3.connect(' NADA.db ')

# criação do cursor
cursor = conn.cursor()

def criarTabela(conn):
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE tb_Usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(70) NOT NULL,
                email VARCHAR(50) NOT NULL,
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

    def inserir(self, usuario, conn):

        cursor = conn.cursor()
        cursor.execute("""
            insert into tb_Usuario(nome,email,nascimento,profissao,genero,publico,senha) values(?,?,?,?,?,?,?)
            """,(usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha))
        conn.commit()

    def listar(self):

        usuarios = []
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


    def atualizar(self,usuario):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Usuario
            set nome = ?,email = ?, nascimento = ?, profissao = ?, genero =?, publico=?, senha=?
            where id = ?
            """, (usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha, id))
        conn.commit()

    def deletar(self):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input('Digite o id:\n'))
        cursor.execute("""
             delete from tb_Usuario
             where id = ?
             """,(id,))

    def solicitarAmizade(self,idEmissor, nome, conn):
        cursor = conn.cursor()

        cursor.execute("""
            select id from tb_Usuario where nome = ?
        """,(nome,))

        idR = cursor.fetchone()[0]

        cursor.execute("""
            insert into tb_Notificacao(texto, emissor,receptor)
            Values(?, ?, ?);
        """,("Solicitacao de Amizade",idEmissor, idR))

        conn.commit()




def listarUsuarios():
    conn = sqlite3.connect(' ifteract.db ')

    usuarios = []
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
