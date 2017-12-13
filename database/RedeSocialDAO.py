import mysql.connector
from model.RedeSocial import RedeSocial
from database.configDB import config

class RedeSocialDAO():

    def inserirRedeSocial(self,redeSocial):

        # Id da Rede Social inserida.
        idRedeSocial = 0
        # Script de Inserção.
        query = "INSERT INTO tb_RedeSocial(nome, descricao, data_criacao) " \
                "VALUES(%s, %s, %s)"
        # Valores.
        values = (redeSocial.nome, redeSocial.descricao, redeSocial.dataCriacao)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id da redesocial inserida no banco.
            if cursor.lastrowid:
                idRedeSocial = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idRedeSocial
