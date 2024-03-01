from  flask import Blueprint, render_template, request
#Blueprint permite el uso de decoradores (variables para trabajar), el render_template asignar html
#Todas estas rutas funcionan por un método get y post
contacts = Blueprint('contacts',__name__)
#Indicamos queu la ruta está relacionada con los contactos, no con app, que solo lo usaremos como configuración
@contacts.route('/')#Decorador
#La ruta es la inicial o la del main, y ejecuta unicamente un método que retorna "Hola inframundo"
def home():
    return render_template("index.html")#Le pasamos este template


@contacts.route('/new',methods=['POST'])
def add_contact():
    print(request.form['fullname'])
    print(request.form['email'])
    print(request.form['phone'])
    return "Guardando un contacto"


@contacts.route('/update')
def update():
    return "Actualizar un contacto"

@contacts.route('/delete')
def delete():
    return "Borrando un contacto"

#Acerca de
@contacts.route('/about')
def about():
    return render_template("about.html")

