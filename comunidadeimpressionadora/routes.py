from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin

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

    return render_template("login.html", form_criarconta = form_criarconta, form_login = form_login)
