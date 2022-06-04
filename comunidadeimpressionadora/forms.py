from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Criar Usuario', validators = [DataRequired()])
    email_criarconta = StringField('Cadastrar Email', validators = [DataRequired(), Email()])
    password_criarconta = PasswordField('Cadastrar Senha', validators = [DataRequired(), Length(6,20)])
    confirm_pass = PasswordField('Confirmar Senha', validators = [DataRequired(), EqualTo('password_criarconta')])
    submit_criarconta = SubmitField('Criar Conta')

    def validate_email_criarconta(self, email_criarconta):
        usuario = Usuario.query.filter_by(email=email_criarconta.data).first()
        if usuario:
            raise ValidationError("Usuario ja cadastrado")

class FormLogin(FlaskForm):
    email_login = StringField('Email', validators = [DataRequired(), Email()])
    password_login = PasswordField('Senha', validators = [DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Usuario', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    foto_perfil = FileField('Editar foto', validators = [FileAllowed(['jpg','png'])])
    curso_excell = BooleanField('Excell')
    curso_powerbi = BooleanField('PowerBi')
    curso_vba = BooleanField('VBA')
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('SQL')
    submit = SubmitField('Confirmar')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuario com esse email!")

class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired(),Length(2,140)])
    corpo = TextAreaField('Escreva seu post', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
