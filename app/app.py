from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def main():
    return "Hello world"

@app.route('/html')
def html():
    return render_template('index.html')


@app.route('/html_dinamico')
def html_dinamico():
    diccionario={
        'saludo':'Saludos',
        'nombre':'Mariana',
    }

    return render_template('dinamico.html',data=diccionario)


@app.route('/pagina_netamente_dinamica')
def funcion():
    cursos=['Programación 3','Base de Datos I','Economía','Perú','Desarrollo Basado en Plataformas','Ecuaciones Diferenciales']

    valores={
        'titulo':'Página totalmente dinámica',
        'saludo':'Saludos',
        'nombre':'Mariana',
        'apellido':'Capuñay',
        'cursos':cursos,
        'cantidad_cursos':len(cursos),
        'fin':True
    }

    return render_template('dinamico_2.html',data=valores)


@app.route('/inicio')
def probando_bloques():
    valores={
        'titulo':"Probando bloques",
        'contenido':'Gracias por utilizar este URL'
    }
    return render_template('inicio.html',dicc=valores)


@app.route('/contacto/<nombre>/<numero>')
def contacto(nombre,numero):  #deben incluirse parametros a solicitar en la funcion
    datos={
        'titulo':'Datos contacto',
        'nombre':nombre,
        'numero':numero
    }
    return render_template('contacto.html',datos_contacto=datos)

@app.route('/main')
def principal():
    return "<h1>Funcion principal</h1>"


@app.route('/request')
def query_string():
    valores=request.args #obteniendo todos los parametros de la URL
    nombre=valores.get('nombre') #obteniendo valor de parametro "nombre"
    apellido=valores.get('apellido') #obteniendo valor de parametro "apellido"
    return "Bienvenid@, "+nombre+" "+apellido #retornando lo que se visualizará en pagina web


def pagina_no_encontrada(error):
    """datos={
        'titulo':'Página no encontrada',
        'mensaje':"Página no existe 😣"
    }

    #forma para retornar mensaje de error
    #return render_template('error.html',error=datos),404   #el 404 es por el n° de error
    """
    #forma para redireccionar
    return redirect(url_for('html'))
    

@app.before_request
def before_request():
    print('Antes de la petición...')
    

@app.after_request
def after_tequest(response):
    print('Después de la petición...')
    return response #aqui se debe retornar "response"


if __name__=='__main__':
    app.add_url_rule('/main_2',view_func=principal)
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()  #esto SIEMPRE debe ir al final del condicional



    

