from django.urls import path
from .views import novoPregao, meusPregoesAbertos, editaPregao, todosAbertos, verPregao, deletePregao, deleteComentario, meusPregoesFechados, meusPregoes #, criarComentario

urlpatterns = [
    path('novo-pregao/', novoPregao, name='novo-pregao'),
    path('pregao/<slug:slug_pregao>/', verPregao, name='visualizar-pregao'),
    path('meus-pregoes/', meusPregoes, name='meus-pregoes'),
    path('pregoes-abertos/', meusPregoesAbertos, name='pregoes-abertos'),
    path('pregoes-fechados/', meusPregoesFechados, name='pregoes-fechados'),
    path('editar-pregao/<slug:slug_pregao>/', editaPregao, name='editar-pregao'),
    path('todos-pregoes/', todosAbertos, name='todos-abertos'),
    path('remove-pregao/<slug:slug_pregao>/', deletePregao, name='remove-pregao'),
    path('remove-comentario/<slug:slug_pregao>/<int:id_comentario>', deleteComentario, name='remove-comentario'),
]