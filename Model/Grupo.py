import sqlite3


def criarTabelaGrupo(conn):
    cursor = conn.cursorGrupo()



    cursor.execute("""
        CREATE TABLE tb_Grupo(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(70) not null,
        data date,
        administrador int not null,
        foreign key (administrador) references tb_Usuario('id')
    
         );
    
    """)



class Grupo():
    def __init__(self, nome, dataCriacao, administrador, participantes = []):
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.administrador = administrador
        self.participantes = participantes
        self.participantes.append(administrador)
        self.moderadors = []

    def inserir(self, grupo, conn):

        cursor = conn.cursor()
        cursor.execute("""
            Select id from tb_Grupo
            where email = ? and senha = ? ;
             
             """, grupo.administrador.email, grupo.administrador.senha)

        idAdmin = cursor.fetchone()

        cursor.execute("""
            insert into tb_Grupo(nome, data, administrador) values(?,?,?)
            """,(grupo.nome,grupo.dataCriacao,idAdmin))
        conn.commit()

    def listar(self, conn):

        cursor = conn.cursor()
        grupos = []
        cursor.execute("""
            Select * From tb_Grupo;
            """)

        for linha in cursor.fetchall():
            nome = linha[1]
            dataCriacao = linha[2]
            admin = linha[3]

        return grupos


    def atualizar(self,grupo,conn):
        cursor = conn.cursor()
        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Grupo
            set nome = ?,dataCriacao = ?, adiministrador
            where id = ?
            """, (grupo.nome,grupo.dataCriacao, grupo.adiministrdor, id))
        conn.commit()

    def deletar(self, conn):

        cursor = conn.cursor()
        id = int(input('Digite o id:\n'))
        cursor.execute("""
             delete from tb_Grupo
             where id = ?
             """,(id,))


