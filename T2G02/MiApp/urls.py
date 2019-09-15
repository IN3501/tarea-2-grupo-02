from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('Contacto/', contacto ,name='contacto'),
    path('inputs/', inputs, name='inputs'),
    path('formulario/', form, name='form'),
    path('registrarse/', registrarse, name='registrarse'),
    path('exitoCrearCuenta/', exitoCrearCuenta, name='exitoCrearCuenta'),
    path('nuevoMensaje/', nuevoMensaje, name='nuevoMensaje'),
    path('inbox/', inbox, name='inbox'),
    path('contactoExitoso/', contactoExitoso, name='contactoExitoso'),
    path('mensajeEnviado/', mensajeEnviado, name="mensajeEnviado"),

]

