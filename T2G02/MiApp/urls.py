from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('avisos/', avisos, name='avisos'),
    path('registrarse/', registrarse, name='registrarse'),
    path('exitoCrearCuenta/', exitoCrearCuenta, name='exitoCrearCuenta'),
    path('agregarAviso/', agregarAviso, name='agregarAviso'),
    path('feedback/', feedback, name='feedback'),
    path('exitofeedback/', exitoFeedback, name='exitofeedback'),

]

