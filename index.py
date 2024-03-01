from app import app
from utils.db import db

if __name__== "__main__":
    app.run(debug=True)
#Ejecutar condicional para iniciar un servidor flask si se hace desde el terminal
with app.app_context():
    db.create_all()

#debug true: Permite que se actualice la página automaticamente sin tener que ejecutar el app.py de continuo