from flask import Flask,  render_template, request
from flask_cors import CORS
from Tabelas.Usuario import *
import sqlite3
import datetime
from Model.Usuario import Usuario, criarTabelaUsuario
from Model.Post import Post, criarTabelaPost
from Model.Grupo import Grupo, criarTabelaGrupo
from Model.Mensagem import Mensagem, criarTabelaMensagem
from Model.Notificacao import Notificacao, criarTabelaNotificacao
from Model.RedeSocial import RedeSocial
from Model import Sistema
import main


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


def main():
    conn = sqlite3.connect("ifteract.db")
    try:
        criarTabelaGrupo(conn)
        criarTabelaNotificacao(conn)
        criarTabelaMensagem(conn)
        criarTabelaUsuario(conn)
        criarTabelaPost(conn)
        conn.commit()
    except:
        print ("Tabela Ja foi Criada")

@app.route("/logar", methods=["POST"])
def logar():
    user = request.json
    usuarios = listarUsuarios()
    perfilEncontrado = False

    for usuario in usuarios:
        if (usuario.email == user["email"]):
            if(usuario.senha == user["senha"]):
                perfilEncontrado = True

    if (perfilEncontrado):
        print(usuario)
        return "UAU", 200

    else:
        return "ERROO", 200

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    usuario = request.json

    nome = usuario["nome"]
    email = usuario["email"]
    nascimento = usuario["nascimento"]
    profissao = usuario["profissao"]
    genero = usuario["genero"]
    publico = usuario["publico"]
    senha = usuario["senha"]

    user  = Usuario(nome,email,nascimento,profissao, genero, publico, senha)

    user.inserir(user,conn)
    return "ok",200

if __name__ == "__main__":

    main()
    app.run()
