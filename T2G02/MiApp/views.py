from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def pestaña(request):
	return render(request, 'pestaña.html')

def inputs(request):
	return render(request, 'inputs.html')

def form(request):
	return render(request, 'form.html')