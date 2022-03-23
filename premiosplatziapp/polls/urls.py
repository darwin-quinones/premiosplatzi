# aqui las urls
from django.urls import path
# el punto indica la importacion de 
# un archivo en la mis carpeta
from . import views
app_name = 'polls' # nombre de la aplicacion para referenciarla

urlpatterns = [
    # se importa la funcion index
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
] 







