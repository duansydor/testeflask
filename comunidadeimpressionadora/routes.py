from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user,login_required

lista_clientes = ['usuA', 'usuB', 'usuB', 'usuC']
redirects_seguros = ['/','/contatos','/clientes','/perfil','/login','/post/criar']
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
        senhacrypt = bcrypt.generate_password_hash(form_criarconta.password_criarconta.data)
        usuario = Usuario(username=form_criarconta.username.data,
                         email=form_criarconta.email_criarconta.data, 
                         password=senhacrypt)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Cadastro feito com sucesso', 'alert-success')
        return redirect(url_for('homepage'))


    if form_login.validate_on_submit() and 'submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email_login.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password,form_login.password_login.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash('Login feito com sucesso {}'.format(usuario.username), 'alert-success')
            #verifica se possui algum redirecionamento next=?
            par_next = request.args.get('next')
            if par_next in redirects_seguros:
                return redirect(par_next)
            else:
                return redirect(url_for('homepage'))
        else:
            flash(f'Email ou senha invalidos', 'alert-danger')

    return render_template("login.html", form_criarconta = form_criarconta, form_login = form_login)

@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash('Usuario desconectado','alert-success')
    return redirect(url_for('homepage'))
@app.route('/post/criar')
@login_required
def criar_post():
    return render_template("criarpost.html")
@app.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html")
