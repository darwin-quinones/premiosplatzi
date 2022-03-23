from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# aquí se crean las funciones
# que llevan a las vistas 
def index(request):
    latest_question_list = Question.objects.all() 
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    # el metodo get_object_or_404 eleva un error 404 en caso de un error en la consulta
    #question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Poll does not exist')
    
    return render(request, 'polls/detail.html', {
        'question': question
    })

def results(request, question_id):
    return HttpResponse(f'<p>Estas viendo los resultado de  la pregunta número {question_id}</p>')


def vote(request, question_id):
    return HttpResponse(f'<p>Estas votando a la pregunta número {question_id}</p>')
