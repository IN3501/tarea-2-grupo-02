from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('avisos/', avisos, name='avisos'),
    path('Contacto/', contacto,name='contacto'),
    path('ContactoLogOut/', contactoLogOut, name='contactologout'),
    path('registrarse/', registrarse, name='registrarse'),
    path('exitoCrearCuenta/', exitoCrearCuenta, name='exitoCrearCuenta'),
    path('nuevoMensaje/', nuevoMensaje, name='nuevoMensaje'),
    path('inbox/', inbox, name='inbox'),
    path('contactoExitoso/', contactoExitoso, name='contactoExitoso'),
    path('contactoExitosoLogOut/', contactoExitosoLogOut, name='contactoExitosoLogOut'),
    path('mensajeEnviado/', mensajeEnviado, name="mensajeEnviado"),
    path('agregarAviso/', agregarAviso, name='agregarAviso'),
    path('feedback/', feedback, name='feedback'),
    path('exitofeedback/', exitoFeedback, name='exitofeedback'),
]

