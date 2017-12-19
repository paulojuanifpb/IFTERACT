import mysql.connector
from model.RedeSocial import RedeSocial
from database.configDB import config
from database.DAO import DAO

class RedeSocialDAO(DAO):

    def __init__(self):
        super(RedeSocialDAO, self).__init__()


    def inserirRedeSocial(self,redeSocial):

        # Id da Rede Social inserida.
        idRedeSocial = 0
        # Script de Inserção.
        query = "INSERT INTO tb_RedeSocial(nome, descricao, data_criacao) " \
                "VALUES(%s, %s, %s)"
        # Valores.
        values = (redeSocial.nome, redeSocial.descricao, redeSocial.dataCriacao)

        try:
            idRedeSocial = super(RedeSocialDAO, self).insert(query,values)
            # Último id da redesocial inserida no banco.

        except mysql.connector.Error as error:
            print(error)

        # Retornar id da rede social.
        return idRedeSocial


    def listar(self):
        # Id da Rede Social inserida.
        idRedeSocial = 0
        redeSocial = None
        # Script de Inserção.
        query = "SELECT * FROM tb_RedeSocial order by id desc"


        try:

            setRedeSocial = super(RedeSocialDAO, self).get_row(query,())



            idRedeSocial = setRedeSocial["id"]

            nome = setRedeSocial["nome"]
            descricao = setRedeSocial["descricao"]
            data_criacao = setRedeSocial["data_criacao"]
            redeSocial = RedeSocial(nome,descricao,data_criacao)


            # Finalizando a persistência dos dados.
        except TypeError as error:
            print(error)

        return (idRedeSocial,redeSocial)
