from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('categorias/', views.Faq.categorias, name='categorias'),
    path('categorias/<int:categ_id>/preguntas/', views.Faq.preguntas, name='preguntas'),
    path('categorias/<int:categ_id>/preguntas/<int:pregunta_id>/respuestas/', views.Faq.respuestas, name='respuestas'),
]
