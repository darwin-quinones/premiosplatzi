# aqui las urls
from django.urls import path
# el punto indica la importacion de 
# un archivo en la mis carpeta
from . import views

urlpatterns = [
    # se importa la funcion index
    path('', views.index, name='index')
] 







