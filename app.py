from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
#Importamos los contactos de la rutas y el SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
#Para poder realizar la conexión le pasamos lo indicado y después los datos de conexión.

app.register_blueprint(contacts) #Usamos el register para imprimir los contactos.
