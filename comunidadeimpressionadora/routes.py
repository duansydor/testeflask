from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin, FormEditarPerfil, FormCriarPost
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user, logout_user, current_user,login_required

redirects_seguros = ['/','/contatos','/clientes','/perfil','/login','/post/criar']
@app.route("/")
def homepage():
    posts = Post.query.order_by(Post.id.desc())
    return render_template("homepage.html", posts = posts)
@app.route("/contatos")
def contatos():
    return render_template("contato.html")
@app.route("/clientes")
def clientes():
    lista_clientes = Usuario.query.all()
    for cliente in lista_clientes:
        cursos = contar_cursos(cliente)
    return render_template("clientes.html", lista_clientes=lista_clientes,cursos=cursos)
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


@app.route('/post/criar',methods=['GET', 'POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo = form.titulo.data, corpo = form.corpo.data, autor = current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso','alert-success')
        return redirect(url_for('homepage'))
    return render_template("criarpost.html", form=form)

def contar_cursos(user):
    lista_cursos = user.cursos.split(';')
    cursos = 0
    if not user.cursos == '':
        cursos = len(lista_cursos)
    else:
        cursos = 0
    return cursos

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    cursos = contar_cursos(current_user)
    return render_template("perfil.html", foto_perfil=foto_perfil,cursos=cursos)
def atualizar_cursos(form):
    cursos = []
    for campo in form:
        if 'curso_' in campo.name and campo.data == True:
            cursos.append(campo.label.text)
    return ';'.join(cursos)

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    cursos = contar_cursos(current_user)
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data

        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash('usuario atualizado com sucesso', 'alert-success')
        return redirect(url_for("perfil"))
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')

    return render_template("editar_perfil.html",foto_perfil=foto_perfil, form=form,cursos=cursos)
