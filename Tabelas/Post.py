import sqlite3

# CONEXÃO
conn = sqlite3.connect(' NADA.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco

def criarTabela(conn):

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE tb_Post (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        texto text not null,
        publico boolean default true
         );
    
    """)


class Post():
    def __init__(self, texto, publico):
        self.texto = texto
        self.publico = publico


    def inserir(self, post):

        cursor.execute("""
            insert into tb_Post(texto, publico) values(?,?)
            """,(post.texto, post.publico))
        conn.commit()

    def listar(self):

        posts = []
        cursor.execute("""
            Select * From tb_Post;
            """)

        for linha in cursor.fetchall():
            texto = linha[0]
            publico = linha[1]
            post = Post(texto, publico)
            posts.append(post)
        return posts


    def atualizar(self,post):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Post
            set teto = ?,publico = ?
            where id = ?
            """, (post.texto,post.publico, id))
        conn.commit()

    def deletar(self):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input('Digite o id:\n'))
        cursor.execute("""
             delete from tb_Post
             where id = ?
             """,(id,))

