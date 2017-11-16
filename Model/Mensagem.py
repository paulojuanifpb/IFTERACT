import sqlite3

# CONEXÃO

# criação das tabelas do banco
def criarTabela(conn):

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE tb_Mensagem(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        texto text not null,
        data date,
        visualizado boolean default false,
        emissor int not null,
        receptor int not null,
        foreign key (emissor) references tb_Usuario('id'),
        foreign key (receptor) references tb_Usuario('id')
         );     
    """)



class Mensagem():
    def __init__(self, texto, data, vizualizado, emissor, receptor):
        self.texto = texto
        self.data = data
        self.vizualizado = vizualizado
        self.emissor = emissor
        self.receptor = receptor

    def inserir(self, mensagem):

        cursor.execute("""
            Select id from tb_Mensagem
            where email = ? and senha = ? ;
             
             """, mensagem.emissor.email, mensagem.emissor.senha)

        idEmissor = cursor.fetchone()

        cursor.execute("""
            insert into tb_Usuario(texto, data, vizualizado, emissor, receptor) values(?,?,?,?,?,?)
            """,(mensagem.texto,mensagem.data,mensagem.vizualizado,idEmissor,mensagem.receptor))
        conn.commit()

    def listar(self):

        mensagens = []
        cursor.execute("""
            Select * From tb_Mensagem;
            """)

        for linha in cursor.fetchall():
            texto = linha[1]
            data = linha[2]
            vizualizado = linha[3]
            idEmissor = linha[4]
            idReceptor = linha[5]
            mensagem = Mensagem(texto, data, vizualizado, idEmissor, idReceptor)
            mensagens.append(mensagem)
        return mensagens


    def atualizar(self,mensagem):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input("digite o id:\n"))
        cursor.execute("""
            update tb_Grupo
            set texto = ?,data = ?, vizualizada = ?, idEmissor = ?, idReceptor = ?
            where id = ?
            """, (mensagem.texto, mensagem.data, mensagem.vizualizado, 1, 2))
        conn.commit()

    def deletar(self):
        conn = sqlite3.connect(' ifteract.db ')

        id = int(input('Digite o id:\n'))
        cursor.execute("""
             delete from tb_Mensagm
             where id = ?
             """,(id,))


