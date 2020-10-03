from .forms import PesquisaForm
from django.contrib.auth.forms import AuthenticationForm

def formulario_login(request):
    return {"login_form": AuthenticationForm(request)}

def formulario_busca(request):
    return {"busca_form": PesquisaForm()}