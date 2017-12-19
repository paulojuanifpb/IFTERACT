import mysql.connector
from database.configDB import config
from model.Notificacao import Notificacao
from model.Usuario import Usuario
from database.UsuarioDAO import UsuarioDAO
from database.DAO import DAO


class NotificacaoDAO(DAO):

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

    def listar(self,idUser):

        notificoesEnviadas = []
        notificoesRecebidas = []

        query = """
            Select * From tb_Notificacao where emissor=%s or receptor=%s;
            """
        values = (idUser, idUser)

        usuarioDAO = UsuarioDAO()

        linhas = super(NotificacaoDAO, self).get_rows (query,values)

        for linha in linhas:
            texto = linha["texto"]
            visualizado = linha["visualizado"]
            confirmar = linha["confirmar"]
            data = linha["data"]
            print(linha["emissor"])
            emissor = usuarioDAO.BuscarUsuarioID(linha["emissor"])
            receptor= usuarioDAO.BuscarUsuarioID(linha["receptor"])

            notificao = Notificacao(texto, visualizado, emissor, receptor, data)
            if (linha["emissor"] == idUser):
                notificoesEnviadas.append(notificao)

            else:
                notificoesRecebidas.append(notificao)

        return (notificoesEnviadas,notificoesRecebidas)

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