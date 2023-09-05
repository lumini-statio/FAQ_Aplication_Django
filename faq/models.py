from django.db import models

# Create your models here.
class Categ(models.Model):
    text = models.CharField(max_length=20)

    def __str__(self):
        return f'categorias {self.text}'


class Question(models.Model):
    text = models.CharField(max_length=80)
    categ = models.ForeignKey(Categ, on_delete = models.CASCADE)

    def __str__(self):
        return f'Pregunta: {self.text}, Categoria: {self.categ}'


class Answer(models.Model):
    text = models.TextField(max_length=400)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'Respuesta {self.text} a {self.question}'

