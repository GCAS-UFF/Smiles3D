from django.urls import path
from .views import cadastro, alterar_senha

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('alterar-senha/', alterar_senha, name='alterar-senha'),
]