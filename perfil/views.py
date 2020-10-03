from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import CustomUser
from pregao.models import Pregao
from .models import Enderecos, PessoaJuridica, PessoaFisica, Avaliacao
from django.contrib.auth.decorators import login_required
from .forms import AvaliacaoForm, PessoaFisicaForm, PessoaJuridicaForm, EnderecoForm
from smiles3d.views import home
from usuario.forms import CadastroForm
from django.contrib import messages
import math

@login_required
def perfil(request, username):
    usuario = get_object_or_404(CustomUser, username=username)
    endereco = get_object_or_404(Enderecos, usuario=usuario.id)
    if(usuario.tipo == "Pessoa Física"):
        perfil = get_object_or_404(PessoaFisica, usuario=usuario.id)
    else:
        perfil = get_object_or_404(PessoaJuridica, usuario=usuario.id)
    avaliacoes = Avaliacao.objects.filter(avaliado=usuario.id)
    pregoes = Pregao.objects.filter(usuario=usuario.id)
    if request.method == "POST":
        form_avaliar = AvaliacaoForm(request.POST)
        if form_avaliar.is_valid():
            avaliacao = form_avaliar.save(commit=False)
            avaliacao.avaliado = usuario
            avaliacao.avaliador = request.user
            avaliacao.save()
            avaliacoes = Avaliacao.objects.filter(avaliado=usuario.id)
            media = 0
            count = 0
            for a in avaliacoes:
                media += a.nota
                count += 1
            resultado = math.floor(media / count)
            perfil.media_avaliacao = resultado
            perfil.save()
    form_avaliar = AvaliacaoForm()
    return render(request, 'perfil/perfil.html', {'usuario': usuario,
                                                   'endereco': endereco,
                                                   'perfil': perfil,
                                                   'avaliacoes': avaliacoes,
                                                   'pregoes': pregoes,
                                                   'form_avaliar': form_avaliar})

def cadastroPessoaFisica(request):
    if request.method == 'POST':
        formpf = PessoaFisicaForm(request.POST, request.FILES)
        if formpf.is_valid():
            cadastro_info = request.session.pop('cadastro', {})
            cadastro_form_instance = CadastroForm(cadastro_info)
            endereco_info = request.session.pop('endereco', {})
            endereco_form_instance = EnderecoForm(endereco_info)
            if endereco_form_instance.is_valid() and cadastro_form_instance.is_valid():
                cadastro_form_instance.save()
                u = get_object_or_404(CustomUser, username=cadastro_info['username'])
                endereco_final = endereco_form_instance.save(commit=False)
                endereco_final.usuario = u
                endereco_final.save()
                perfilpf = formpf.save(commit=False)
                perfilpf.usuario = u
                perfilpf.save()
                return redirect(home)
            else:
                messages.add_message(request, messages.INFO, endereco_form_instance.errors)
                messages.add_message(request, messages.INFO, cadastro_form_instance.errors)
                return render(request, 'perfil/cadastro-pf.html', {'formPF': formpf})
        else:
            messages.add_message(request, messages.INFO, formpf.errors)
    formpf = PessoaFisicaForm()
    return render(request, 'perfil/cadastro-pf.html', {'formPF': formpf})

def cadastroPessoaJuridica(request):
    if request.method == 'POST':
        formpj = PessoaJuridicaForm(request.POST, request.FILES)
        if formpj.is_valid():
            cadastro_info = request.session.pop('cadastro', {})
            cadastro_form_instance = CadastroForm(cadastro_info)
            endereco_info = request.session.pop('endereco', {})
            endereco_form_instance = EnderecoForm(endereco_info)
            if endereco_form_instance.is_valid() and cadastro_form_instance.is_valid():
                cadastro_form_instance.save()
                u = get_object_or_404(CustomUser, username=cadastro_info['username'])
                endereco_final = endereco_form_instance.save(commit=False)
                endereco_final.usuario = u
                endereco_final.save()
                perfilpj = formpj.save(commit=False)
                perfilpj.usuario = u
                perfilpj.save()
                return redirect(home)
            else:
                messages.add_message(request, messages.INFO, endereco_form_instance.errors)
                messages.add_message(request, messages.INFO, cadastro_form_instance.errors)
                return render(request, 'perfil/cadastro-pf.html', {'formPF': formpj})
        else:
            messages.add_message(request, messages.INFO, formpj.errors)
    formpj = PessoaJuridicaForm()
    return render(request, 'perfil/cadastro-pf.html', {'formPF': formpj})

def excluirAvaliacao(request, id_avaliacao, id_usuario):
    usuario = get_object_or_404(CustomUser, pk=id_usuario)
    if (usuario.tipo == "Pessoa Física"):
        perfil = get_object_or_404(PessoaFisica, usuario=id_usuario)
    else:
        perfil = get_object_or_404(PessoaJuridica, usuario=id_usuario)
    avaliacao = get_object_or_404(Avaliacao, pk=id_avaliacao)
    avaliacao.delete()
    avaliacoes = Avaliacao.objects.filter(avaliado=id_usuario)
    media = 0
    count = 0
    for a in avaliacoes:
        media += a.nota
        count += 1
    resultado = math.floor(media / count)
    perfil.media_avaliacao = resultado
    perfil.save()
    messages.add_message(request, messages.INFO, 'Avaliação excluída com sucesso!')
    return redirect('perfil', usuario.username)