from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    print("Comeco")
    return render_template("layout.html"), 200



@app.route("/cadastrar")
def cadastrar():
    usuario = request.json()
    print(usuario)

    return "ok",200

if __name__ == "__main__":
    app.run()
