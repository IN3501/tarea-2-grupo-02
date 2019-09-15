from django.shortcuts import render


# Create your views here.
def index(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'password':
                nombre = request.POST['inputText']
                if nombre:
                    return render(request, 'home.html',
                                  {'name': nombre}
                                   )
    return render(request, 'home.html')
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
                           'type':type,
                           'day':s.join(day)
                           })
    return render(request, 'avisos.html')


def registrarse(request):
    if request.method == 'POST':
        return render(request, 'mensajeDeExito.html')
    else:
        return render(request, 'formNuevaCuenta.html')
def feedback(request):
    return render(request,'formulariotarea2.html')
def exitoFeedback(request):
    if request is not None:
        if request.method == 'POST':
            if 'inputText' and 'inputEmail' and 'inputPassword':
                nombre = request.POST['inputText']
                materia = request.POST['materia']
                descripcion = request.POST['descripcion']
                if nombre and materia and descripcion:
                    mensaje = "Hemos enviado tu feedback a " + nombre + ", con quien tuviste clases de  " + \
                              materia+" con el siguiente comentario "+descripcion
                    return render(request, 'mensajeDeExitoLogOut.html',
                                  {'titleMessage': "Feedback enviado con exito",
                                   'message': mensaje})
    return render(request,'formulariotarea2.html')

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
def agregarAviso(request):
    return render(request, 'formAgregarAviso.html')