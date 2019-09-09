from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('pestaña/', pestaña ,name='pestaña'),
    path('inputs/', inputs, name='inputs'),
    path('formulario/', form, name='form'),
    path('registrarse/', registrarse, name='registrarse'),
    path('exitoCrearCuenta/', exitoCrearCuenta, name='exitoCrearCuenta'),

]

