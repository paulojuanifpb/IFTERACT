from flask import Flask,  render_template, request
from Tabelas.Usuario import *
import sqlite3
import datetime
from Model import Usuario, criarTabela
from Model import Post, criarTabela
from Model import Grupo, criarTabela
from Model import Mensagem, criarTabela
from Model import Notificação, criarTabela
from Model import RedeSocial, criarTabela
from Model import Sistema, criarTabela

app = Flask(__name__)


def main():

    conn = sqlite3.connect("ifteract.db")
    try:
        Grupo.criarTabela(conn)
        Notificação.criarTabela(conn)
        Mensagem.criarTabela(conn)
        Post.criarTabela(conn)
        Usuario.criarTabela(conn)
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
        return render_template("home.html"), 200

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
