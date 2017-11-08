from flask import Flask,  render_template, request
from Tabelas.Usuario import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def loginCadastro():
    print("Comeco")
    return render_template("login.html"), 200


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
        return "ACHOU", 200

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

    user.inserir(user)
    return "ok",200

if __name__ == "__main__":

    app.run()
