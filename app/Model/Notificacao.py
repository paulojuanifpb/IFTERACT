import sqlite3

# CONEXÃO
conn = sqlite3.connect(' NADA.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
def criarTabelaNotificacao(conn):

    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE tb_Notificacao(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            texto VARCHAR(100),
            confirmar boolean default false,
            visualizado boolean default false,
            emissor int not null,
            receptor int not null,
            foreign key (emissor) references tb_Usuario('id'),
            foreign key (receptor) references tb_Usuario('id')
        
             );
        
        """)


class Notificacao():
    def __init__(self, texto, data, confirmar, vizualizado, emissor, receptor):
        self.texto = texto
        self.data = data
        self.confirmar =confirmar
        self.vizualizado = vizualizado
        self.emissor = emissor
        self.receptor = receptor

    def inserir(self, notificacao, emissor, conn):

        cursor = conn.cursor()
        idEmissor = cursor.fetchone()

        cursor.execute("""
            insert into tb_Usuario(texto, data, confirmar, vizulizado, emissor, receptor) values(?,?,?,?,?,?)
            """,(notificacao.texto,notificacao.data,notificacao.confirmar ,notificacao.vizualizado,idEmissor,notificacao.receptor))
        conn.commit()

    def listar(self):

        notificacoes = []
        cursor.execute("""
            Select * From tb_Notificao;
            """)

        for linha in cursor.fetchall():
            texto = linha[1]
            data = linha[2]
            confirmar = linha[3]
            vizualizado = linha[4]
            idEmissor = linha[5]
            idReceptor = linha[6]
            notificacao = Notificacao(texto, data, confirmar, vizualizado, idEmissor, idReceptor)
            notificacoes.append(notificacao)
        return notificacoes


    def atualizar(self,notificacao):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Grupo
            set texto = ?,data = ?, confirmar = ?, vizualizada = ?, idEmissor = ?, idReceptor = ?
            where id = ?
            """, (notificacao.texto, notificacao.data,  notificacao.vizualizado, 1, 2))
        conn.commit()

    def deletar(self):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input('Digite o id:\n'))
        cursor.execute("""
             delete from tb_Notificacao
             where id = ?
             """,(id,))


