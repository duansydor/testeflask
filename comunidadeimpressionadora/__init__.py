from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = "d55f9e8bae98dc2af9422509f6ed4a5a"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from comunidadeimpressionadora import routes