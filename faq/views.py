from django.shortcuts import render, get_object_or_404
from .models import *

class Faq:
    def categorias(request):
        template_name = 'faq/categ.html'
        categs = Categ.objects.all()
        context = {
            'categs': categs,
        }
        return render(request, template_name, context)

    def preguntas(request, categ_id):
        template_name = 'faq/quests.html'
        categ = get_object_or_404(Categ, id=categ_id)
        preguntas = categ.question_set.all()
        context = {
            'preguntas': preguntas,
            'categ': categ,
        }
        return render(request, template_name, context)

    def respuestas(request, categ_id, pregunta_id):
        template_name = 'faq/ans.html'
        pregunta = get_object_or_404(Question, id=pregunta_id)
        respuestas = pregunta.answer_set.all()
        context = {
            'pregunta': pregunta,
            'respuestas': respuestas,
        }
        return render(request, template_name, context)