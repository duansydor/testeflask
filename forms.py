from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Criar Usuario', validators = [DataRequired()])
    email_criarconta = StringField('Cadastrar Email', validators = [DataRequired(), Email()])
    password_criarconta = PasswordField('Cadastrar Senha', validators = [DataRequired(), Length(6,20)])
    confirm_pass = PasswordField('Confirmar Senha', validators = [DataRequired(), EqualTo('password_criarconta')])
    submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email_login = StringField('Email', validators = [DataRequired(), Email()])
    password_login = PasswordField('Senha', validators = [DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    submit_login = SubmitField('Fazer Login')