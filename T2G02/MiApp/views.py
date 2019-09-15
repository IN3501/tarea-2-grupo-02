from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def contacto(request):
	if request.method =='POST':
		return render(request, 'contactoExitoso.html')
	else:
		return render(request, 'Contacto.html')

def inputs(request):
	return render(request, 'inputs.html')

def form(request):
	return render(request, 'form.html')

def registrarse(request):
	if request.method == 'POST':
		return render(request, 'mensajeDeExito.html')
	else:
		return render(request, 'formNuevaCuenta.html')

def contactoExitoso(request):
	if request is not None:
		if request.method == 'POST':
			if 'inputText' and 'inputEmail' and 'Coment':
				nombre=request.POST['inputText']
				email=request.POST['inputEmail']
				coment=request.POST['Coment']
				return render(request, 'contactoExitoso.html')
	return render(request, 'contacto.html')

def mensajeEnviado(request):
	if request is not None:
		if request.method == 'POST':
			if 'inputText' and 'inputEmail' and 'inputEmail2' and 'quien'and'Coment' :
				nombre=request.POST['inputText']
				email=request.POST['inputEmail']
				destino=request.POST['quien']
				email=request.POST['inputEmail2']
				coment=request.POST['Coment']
				return render(request, 'mensajeEnviado.html')
	return render(request, 'nuevoMensaje.html')

def exitoCrearCuenta(request):
	if request is not None:
		if request.method =='POST':
			if 'inputText' and 'inputEmail' and 'inputPassword':
				nombre =request.POST['inputText']
				email =request.POST['inputEmail']
				password = request.POST['inputPassword']
				if nombre and email and password:
					mensaje="Felicidades "+nombre+", se ha creado tu cuenta con el correo " + email
					return render(request, 'mensajeDeExitoLogOut.html',
								  {'titleMessage':"Cuenta creada con exito",
									  'message': mensaje})

	return render(request, 'formNuevaCuenta.html')

def nuevoMensaje(request):
	if request.method == 'POST':
		return render(request, 'mensajeEnviado.html')
	else:
		return render(request, 'nuevoMensaje.html')

def inbox(request):
	return render(request, 'inbox.html')
