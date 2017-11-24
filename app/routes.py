from flask import Flask, render_template, request
import sqlite3
import json
import datetime
from Model.Usuario import Usuario, criarTabelaUsuario, listarUsuarios
from Model.Post import Post, criarTabelaPost
from Model.Grupo import Grupo, criarTabelaGrupo
from Model.Mensagem import Mensagem, criarTabelaMensagem
from Model.Notificacao import Notificacao, criarTabelaNotificacao
from Model.RedeSocial import RedeSocial
from Model import Sistema

app = Flask(__name__)

conn = sqlite3.connect("ifteract.db")


def default_parser(obj):
    if getattr(obj, "__dict__", None):
        return obj.__dict__
    elif type(obj) == datetime:
        return obj.isoformat()
    else:
        return str(obj)



def main():
    try:
        criarTabelaGrupo(conn)
        criarTabelaNotificacao(conn)
        criarTabelaMensagem(conn)
        criarTabelaUsuario(conn)
        criarTabelaPost(conn)
        conn.commit()
    except:
        print ("Tabela Ja foi Criada")

@app.route("/", methods=["GET"])
def loginCadastro():
    print("Comeco")
    return render_template("login.html"), 200


@app.route("/logar", methods=["POST"])
def logar():
    user = request.json
    usuarios = listarUsuarios(conn)
    perfilEncontrado = False


    for usuario in usuarios:
        if (usuario.email == user["email"]):
            if(usuario.senha == user["senha"]):
                perfilEncontrado = True

                print("Mas Chegou")
                userJSON = json.dumps(usuario, default=default_parser)
                print(userJSON)

                return userJSON, 200



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

    user.inserir(user, conn)
    return "ok",200

@app.route("/home", methods=["GET"])
def home():
    print ("Pelo Menos Chegou Aqui")

    return render_template("home.html"), 200


@app.route("/inf", methods=["GET"])
def inf():
    user = listarUsuarios(conn)[0]
    return (json.dumps(user, default=default_parser), 200)

if __name__ == "__main__":
    main()
    app.run()
