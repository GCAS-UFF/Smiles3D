from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .forms import PesquisaForm, ContatoForm
from pregao.models import Pregao
from usuario.models import CustomUser
from perfil.models import PessoaJuridica, PessoaFisica
from django.contrib import messages

def home(request):
    return render(request, 'smiles3d/home.html')

def sobre(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if(form.is_valid()):
            messages.add_message(request, messages.INFO, 'Mensagem enviada com sucesso! Enviaremos para o e-mail informado '
                                                         'uma resposta em breve!.')
        else:
            messages.add_message(request, messages.INFO, 'Não foi possível enviar sua mensagem. '
                                                         'Por favor, tente novamente mais tarde.')
    form = ContatoForm()
    return render(request, 'smiles3d/sobre.html', {'form': form})

def pesquisa(request):
    form = PesquisaForm(request.GET)
    if (form.is_valid()):
        busca_por = form.cleaned_data['busca_por']
        lista_pregoes = Pregao.objects.filter(tipo__icontains=busca_por).order_by('data')
        lista_de_usuarios = CustomUser.objects.filter(username__icontains=busca_por).order_by('username')
        lista_de_perfis = []
        for u in lista_de_usuarios:
            if u.tipo == "Pessoa Física":
                lista_de_perfis.append(get_object_or_404(PessoaFisica, usuario=u.id))
            else:
                lista_de_perfis.append(get_object_or_404(PessoaJuridica, usuario=u.id))
        usuarios = zip(lista_de_usuarios, lista_de_perfis)
        return render(request, 'smiles3d/busca.html', {'pregoes': lista_pregoes,
                                                       'usuarios': usuarios,
                                                        'busca_por': busca_por})
    else:
        raise ValueError('Ocorreu um erro inesperado ao realizar a pesquisa.')
