import sqlite3

# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
cursor.execute("""
    CREATE TABLE tb_Usuario (
        id int auto_increment primary key,
        nome VARCHAR(70) NOT NULL,
        email VARCHAR(50) NOT NULL,
        nascimento DATE,
        profissao VARCHAR(50),
        genero VARCHAR(10),
        publico BOOLEAN default FALSE,
        senha VARCHAR(30) NOT NULL
     );

""")


conn.close()


class Usuario():
    def __init__(self, nome, email, nascimento, profissao, genero, publico, senha):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento
        self.profissao = profissao
        self.genero = genero
        self.publico = publico
        self.senha = senha

    def inserir(self, usuario):
        cursor.execute("""
            insert into tb_Usuario values(?,?,?,?,?,?,?)
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
        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Usuario
            set nome = ?,email = ?, nascimento = ?, profissao = ?, genero =?, publico=?, senha=?
            where id = ?
            """, (usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha, id))
        conn.commit()

    def deletar(self):
         id = int(input('Digite o id:\n'))
         cursor.execute("""
             delete from tb_Usuario
             where id = ?
             """,(id,))

