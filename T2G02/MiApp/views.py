from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'MiApp/index.html')

def pestaña(request):
	return render(request, 'MiApp/pestaña.html')