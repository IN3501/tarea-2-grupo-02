from django.shortcuts import render


# Create your views here.
def index(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'password':
                nombre = request.POST['inputText']
                if nombre:
                    return render(request, 'home.html', {'name': nombre})
    return render(request, 'home.html')


def contacto(request):
    return render(request, 'contactologin.html')
def contactoLogOut(request):
    return render(request, 'contactologout.html')


def inputs(request):
    return render(request, 'avisos.html')


def login(request):
    return render(request, 'login.html')


def avisos(request):
    if request.method == 'POST':
        name = request.POST['inputText']
        type = request.POST['type']
        day = request.POST.getlist("day")
        s = ", "
        if name and type and day:
            return render(request, 'avisos.html',
                          {'name': name,
                           'type': type,
                           'day': s.join(day)
                           })
    return render(request, 'avisos.html')


def registrarse(request):
    if request.method == 'POST':
        return render(request, 'mensajeDeExito.html')
    else:
        return render(request, 'formNuevaCuenta.html')


def feedback(request):
    return render(request, 'formulariotarea2.html')


def exitoFeedback(request):
    if request is not None:
        if request.method == 'POST':
            if 'grade'and 'inputText' and 'inputEmail' and 'inputPassword':
                nombre = request.POST['inputText']
                materia = request.POST['materia']
                descripcion = request.POST['descripcion']
                nota=request.POST["grade"]
                if nombre and materia and descripcion:
                    mensaje = "Hemos enviado tu feedback a " + nombre + ", con quien tuviste clases de  " + \
                              materia + " con el siguiente comentario " + descripcion + "y la siguiente nota:"+nota
                    return render(request, 'mensajeDeExitoLogOut.html',
                                  {'titleMessage': "Feedback enviado con exito",
                                   'message': mensaje})
    return render(request, 'formulariotarea2.html')


def contactoExitoso(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'inputEmail' and 'Coment':
                nombre = request.POST['inputText']
                email = request.POST['inputEmail']
                coment = request.POST['Coment']
                mensaje = "Hola " + nombre + ", hemos recibido tu mensaje: " + \
                          coment + ", com el correo: " + email + ", te contactaremos a la brevedad"
                return render(request, 'mensajeDeExito.html',
                              {'titleMessage': "¡Gracias por contactarnos!",
                               'message': mensaje})
    return render(request, 'contacto.html')

def contactoExitosoLogOut(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'inputEmail' and 'Coment':
                nombre = request.POST['inputText']
                email = request.POST['inputEmail']
                coment = request.POST['Coment']
                mensaje = "Hola " + nombre + ", hemos recibido tu mensaje: " + \
                          coment + ", com el correo: " + email + ", te contactaremos a la brevedad"
                return render(request, 'mensajeDeExitoLogOut.html',
                              {'titleMessage': "¡Gracias por contactarnos!",
                               'message': mensaje})
    return render(request, 'contacto.html')

def mensajeEnviado(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'inputEmail' and 'inputEmail2' and 'quien' and 'Coment':
                nombre = request.POST['inputText']
                email1 = request.POST['inputEmail']
                destino = request.POST['quien']
                email2 = request.POST['inputEmail2']
                coment = request.POST['Coment']
                mensaje="Hemos enviado tu mensaje:"+coment + " al "+ destino+" llamado "+nombre+" cuyo correo es:" + email2+" .El usuario se pondrá en contacto contigo al correo: "+email1
                return render(request, 'mensajeDeExitoLogOut.html',
                              {'titleMessage': "¡Hemos contacto al usuario "+nombre+"!",
                               'message': mensaje})
    return render(request, 'nuevoMensaje.html')


def exitoCrearCuenta(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'inputEmail' and 'inputPassword':
                nombre = request.POST['inputText']
                email = request.POST['inputEmail']
                password = request.POST['inputPassword']
                if nombre and email and password:
                    mensaje = "Felicidades " + nombre + ", se ha creado tu cuenta con el correo " + email
                    return render(request, 'mensajeDeExitoLogOut.html',
                                  {'titleMessage': "Cuenta creada con exito",
                                   'message': mensaje})
        return render(request, 'formNuevaCuenta.html')


def nuevoMensaje(request):
    if request.method == 'POST':
        return render(request, 'mensajeEnviado.html')
    else:
        return render(request, 'nuevoMensaje.html')


def inbox(request):
    return render(request, 'inbox.html')


def agregarAviso(request):
    return render(request, 'formAgregarAviso.html')
