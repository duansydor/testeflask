from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Usuario', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Senha', validators = [DataRequired(), Length(6,20)])
    confirm_pass = PasswordField('Confirmar Senha', validators = [DataRequired(), EqualTo('Password')])
    submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Senha', validators = [DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    submit_login = SubmitField('Fazer Login')
