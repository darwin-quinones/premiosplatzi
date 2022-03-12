from django.shortcuts import render
from django.http import HttpResponse

# aquí se crean las funciones
# que llevan a las vistas 
def index(request):
    return HttpResponse('Hello World')
