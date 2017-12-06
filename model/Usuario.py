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

    def inserir(self, usuario, conn):

        try:

            cursor = conn.cursor()
            cursor.execute("""
                insert into tb_Usuario(nome,email,nascimento,profissao,genero,publico,senha) values(?,?,?,?,?,?,?)
                """,(usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Ese Endereco de email ja está sendo usado em outra conta")

    def listar(self,conn):

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

    def solicitarAmizade(self,idEmissor, email, conn):
        cursor = conn.cursor()

        try:
            cursor.execute("""
                select id from tb_Usuario where email = ?
            """,(email,))

            idR = cursor.fetchone()[0]

            cursor.execute("""
                insert into tb_Notificacao(texto, emissor,receptor)
                Values(?, ?, ?);
            """,("Solicitacao de Amizade",idEmissor, idR))

            conn.commit()

        except TypeError:
            print("Nao  foi encontrado ninguem com esse email")


    def enviarMensagem(self, texto, idEmissor, idReceptor,conn):

        cursor = conn.cursor()
        cursor.execute("""
        Insert into tb_Mensagem(texto, emissor, receptor)
        Values(?,?,?);
        """,(texto, idEmissor, idReceptor))

        conn.commit()

    def aceitarSolicitacao(self, idUsuario, conn):
        email = input("DIgite o email do usuario que fez a solicitacao")
        cursor = conn.cursor()

        cursor.execute("""
            Select id from tb_Usuario where email = ?
        """,(email,))

        idEmissor = cursor.fetchone()[0]
        print(idEmissor)

        cursor.execute("""
            update tb_Notificacao
            set confirmar = 'true', visualizado = 'true' where emissor = ? and receptor = ?;

         """,(idEmissor, idUsuario))

        conn.commit()


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
