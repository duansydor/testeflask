from flask import Flask, render_template, url_for, request,flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "d55f9e8bae98dc2af9422509f6ed4a5a"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

lista_clientes = ['usuA', 'usuB', 'usuB', 'usuC']

database = SQLAlchemy(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contato.html")
@app.route("/clientes")
def clientes():
    return render_template("clientes.html", lista_clientes=lista_clientes)
@app.route("/login", methods=['GET', 'POST'])
def login():
    form_criarconta = FormCriarConta()
    form_login = FormLogin()

    if form_criarconta.validate_on_submit() and 'submit_criarconta' in request.form:
        flash(f'Cadastro feito com sucesso', 'alert-success')
        return redirect(url_for('homepage'))


    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f'Login feito com sucesso ', 'alert-success')
        return redirect(url_for('homepage'))

    if form_criarconta.validate_on_submit() and 'submit_criarconta' in request.form:
        flash(f'Cadastro feito com sucesso', 'alert-success')
        return redirect(url_for('homepage'))


    return render_template("login.html", form_criarconta = form_criarconta, form_login = form_login)

if __name__ == '__main__':
    app.run(debug=True)