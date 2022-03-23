from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    # no es necesario poner el id
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    ## method to ver los strings
    def __str__(self):
        return self.question_text
    
    # metodo para saber si fue reciente o no la publicacion
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # la clase meta me permite renombrar el modelo
    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = ("Preguntas de la encuenta")
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    class Meta:
        verbose_name_plural = ('Respuestas de las preguntas')
