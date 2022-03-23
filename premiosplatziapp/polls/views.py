from django.shortcuts import render
from django.http import HttpResponse

# aquí se crean las funciones
# que llevan a las vistas 
def index(request):
    return HttpResponse('Estas en la pagina principal de Premios Platzi  App')


def detail(request, question_id):
    return HttpResponse(f'<p>Estas viendo la pregunta número {question_id}</p>')

def results(request, question_id):
    return HttpResponse(f'<p>Estas viendo los resultado de  la pregunta número {question_id}</p>')


def vote(request, question_id):
    return HttpResponse(f'<p>Estas votando a la pregunta número {question_id}</p>')
