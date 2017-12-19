from database.configDB import config
import mysql.connector
from model.Usuario import Usuario
from database.DAO import DAO


class UsuarioDAO(DAO):
    
    def __init__(self):
        super(UsuarioDAO, self).__init__()
    
    
    def inserir(self, usuario):

        try:

            query =  """
                insert into tb_Usuario(nome,email,nascimento,profissao,genero,publico,senha) values(%s, %s, %s, %s, %s, %s, %s)
                """
            values = (usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha)

            super(UsuarioDAO, self).insert(query,values)

        except mysql.connector.Error as error:
            print(error)


    def listar(self):

        usuarios = []

        query = """
            Select * From tb_Usuario;
            """

        resultado = super(UsuarioDAO, self).get_rows(query,())

        for linha in resultado:
            nome = linha["nome"]
            email = linha["email"]
            nascimento = linha["nascimento"]
            profissao = linha["profissao"]
            genero = linha["genero"]
            publico = linha["publico"]
            senha = linha["senha"]
            usuario = Usuario(nome, email, nascimento, profissao, genero, publico, senha)
            usuarios.append(usuario)


        return usuarios

    '''
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

    '''

    def solicitarAmizade(self,idEmissor, email):

        #escolha = int(input("1-Digite um para Solicitar via email ou"))

        try:
            query = """
                select id from tb_Usuario where email = %s
            """

            idR = super(UsuarioDAO, self).get_row(query, (email,))["id"]


            query = """
                insert into tb_Notificacao(texto, emissor,receptor) Values(%s, %s, %s);
            """

            values = ("Solicitacao de Amizade",idEmissor, idR)

            super(UsuarioDAO, self).insert(query,values)

        except TypeError:
            print("Nao  foi encontrado ninguem com esse email")


    def enviarMensagem(self, texto, idEmissor, email):


        try:

            query = """
                select id from tb_Usuario where email = %s
            """

            values = (email,)

            idReceptor = super(UsuarioDAO, self).get_row(query, values)["id"]

            query = """
                Select confirmar from tb_Notificacao where emissor = %s and receptor = %s;
            """

            values =  (idReceptor, idEmissor)

            confirmacao = super(UsuarioDAO, self).get_row(query, values)["confirmar"]

            if (confirmacao == "true"):

                texto = input("Digite a sua mensagem\n")


                query = """
                        Insert into tb_Mensagem(texto, emissor, receptor)
                        Values(%s, %s, %s);
                        """
                values = (texto, idEmissor, idReceptor)

                super(UsuarioDAO, self).insert(query, values)


            else:
                print("Amigo Nao encontrado")



        except TypeError:
            print("Email não encontrado")

    def aceitarSolicitacao(self, idUsuario):

        email = input("DIgite o email do usuario que fez a solicitacao")

        query = """
           Select id from tb_Usuario where email = %s
        """

        idEmissor = super(UsuarioDAO, self).get_row(query,(email,))["id"]


        query = """
            update tb_Notificacao set confirmar = true, visualizado = true where emissor = %s and receptor = %s;

         """

        values = (idEmissor, idUsuario)
        print(values)

        super(UsuarioDAO, self).execute(query,values)


    def desfazerAmizade(self, idUsuario):



        email = input("DIgite o email do usuario que fez a solicitacao")

        query = """
                    Select id from tb_Usuario where email = %s
                """

        values = (email,)

        idEmissor = super(UsuarioDAO, self).get_row(query,values)["id"]
        print(idEmissor)

        query = """
            delete from tb_Notificacao where emissor= %s and receptor= %s or receptor= %s and emissor=%s;
        
        """

        values = (idUsuario, idEmissor, idUsuario, idEmissor)

        super(UsuarioDAO, self).execute(query,values)

    def BuscarUsuarioID(self,idUsuario):



        query = """
            Select * from tb_Usuario where id = %s
        """




        linha = super(UsuarioDAO, self).get_row(query,(idUsuario,))

        nome = linha["nome"]
        email = linha["email"]
        nascimento = linha["nascimento"]
        profissao = linha["profissao"]
        genero = linha["genero"]
        publico = linha["publico"]
        senha = linha["senha"]
        usuario = Usuario(nome, email, nascimento, profissao, genero, publico, senha)

        return usuario

    def buscarUsuarioNome(self):

        nome = str(input("Digite o nome do Usuario:"))
        usuarios = []

        query = """
            Select nome, email
            from tb_Usuario
            Where nome like '%%s%'
        
        """

        resultado = super(UsuarioDAO, self).get_rows(query, (nome,))

        for linha in resultado():
            nome = linha["nome"]
            email = linha["email"]
            nascimento = linha["nascimento"]
            profissao = linha["profissao"]
            genero = linha["genero"]
            publico = linha[publico]
            senha = linha["senha"]
            usuario = Usuario(nome, email, nascimento, profissao, genero, publico, senha)
            usuarios.append(usuario)

        return usuarios



