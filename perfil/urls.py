from django.urls import path
from .views import perfil, cadastroPessoaFisica, cadastroPessoaJuridica, excluirAvaliacao #, perfilsuccess, fotoPerfil_change,

urlpatterns = [
    path('perfil/<str:username>', perfil, name='perfil'),
    path('cadastro/pessoa-fisica', cadastroPessoaFisica, name='cadastro-pf'),
    path('cadastro/pessoa-juridica', cadastroPessoaJuridica, name='cadastro-pj'),
    path('excluir-avaliacao/<int:id_avaliacao>/<int:id_usuario>', excluirAvaliacao, name='excluir-avaliacao'),
]
