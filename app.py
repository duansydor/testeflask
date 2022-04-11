from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin
app = Flask(__name__)
app.config['SECRET_KEY'] = "d55f9e8bae98dc2af9422509f6ed4a5a"
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
    form_criarconta = FormCriarConta()
    form_login = FormLogin()
    return render_template("login.html", form_criarconta = form_criarconta, form_login = form_login)

if __name__ == '__main__':
    app.run(debug=True)