from flask import Flask,  render_template, request
from flask_cors import CORS
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

cors = CORS(app, resources={r"/*": {"origins": "*"}})

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
        print("Esta Criando As Tabelas")
        criarTabelaGrupo(conn)
        criarTabelaNotificacao(conn)
        criarTabelaMensagem(conn)
        criarTabelaUsuario(conn)
        criarTabelaPost(conn)
        print("Ele criou a tabelas")
    except:
        print ("Tabela Ja foi Criada")

@app.route("/logar", methods=["POST"])
def logar():
    user = request.json
    usuarios = listarUsuarios(conn)
    perfilEncontrado = False

    for usuario in usuarios:
        if (usuario.email == user["email"]):
            if(usuario.senha == user["senha"]):
                perfilEncontrado = True

                userJSON = json.dumps(usuario, default=default_parser)
                print(userJSON)
                return (json.dumps(usuario, default=default_parser), 200)

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
