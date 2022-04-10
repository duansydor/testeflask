from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_clientes = ['usuA', 'usuB', 'usuB', 'usuC']

@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contato.html")
@app.route("/clientes")
def clientes():
    return render_template("clientes.html", lista_clientes=lista_clientes)
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)