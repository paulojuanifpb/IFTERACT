from database.configDB import config
import mysql.connector
from model.Usuario import Usuario

class UsuarioDAO():
    def inserir(self, usuario):

        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute( """
                insert into tb_Usuario(nome,email,nascimento,profissao,genero,publico,senha) values(%s, %s, %s, %s, %s, %s, %s)
                """,(usuario.nome,usuario.email,usuario.nascimento,usuario.profissao,usuario.genero,usuario.publico,usuario.senha))
            conn.commit()
        except mysql.connector.Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

    def listar(self):

        conn = mysql.connector.connect(**config)
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

        cursor.close()
        conn.close()
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

    def solicitarAmizade(self,idEmissor, email):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                select id from tb_Usuario where email = %s
            """,(email,))

            idR = cursor.fetchone()[0]

            cursor.execute("""
                insert into tb_Notificacao(texto, emissor,receptor)
                Values(%s, %s, %s);
            """,("Solicitacao de Amizade",idEmissor, idR))

            conn.commit()

            cursor.close()
            conn.close()

        except TypeError:
            print("Nao  foi encontrado ninguem com esse email")


    def enviarMensagem(self, texto, idEmissor, idReceptor):

        conn = mysql.connector.connect(**config)

        cursor = conn.cursor()
        cursor.execute("""
        Insert into tb_Mensagem(texto, emissor, receptor)
        Values(%s,%s,%s);
        """,(texto, idEmissor, idReceptor))


        conn.commit()
        cursor.close()
        conn.close()


    def aceitarSolicitacao(self, idUsuario):

        conn = mysql.connector.connect(**config)
        email = input("DIgite o email do usuario que fez a solicitacao")
        cursor = conn.cursor()

        cursor.execute("""
            Select id from tb_Usuario where email = %s
        """,(email,))

        idEmissor = cursor.fetchone()[0]
        print(idEmissor)

        cursor.execute("""
            update tb_Notificacao
            set confirmar = true, visualizado = true where emissor = %s and receptor = %s;

         """,(idEmissor, idUsuario))

        conn.commit()
        cursor.close()
        conn.close()