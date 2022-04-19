from app import database

class Usuario(database.Model):
    id = database.Collumn(databse.Integer, primary_key = True)
    username = database.Collumn()
    email = database.Collumn()
    password = database.Collumn()
    foto_perfil = database.Collumn()