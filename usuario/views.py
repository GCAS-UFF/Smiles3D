from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from .decorators import check_recaptcha
from django.contrib import messages
from perfil.forms import EnderecoForm, PessoaJuridicaForm, PessoaFisicaForm
from .forms import CadastroForm
from smiles3d.views import home
from django.contrib import messages

@check_recaptcha
def cadastro(request):
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST, prefix="cadastro")
        form_endereco = EnderecoForm(request.POST, prefix="endereco")
        if form_cadastro.is_valid() and form_endereco.is_valid():
            if form_cadastro.cleaned_data["tipo"] == "Pessoa Jurídica":
                form_perfil = PessoaJuridicaForm(request.POST, request.FILES, prefix="juridica")
            else:
                form_perfil = PessoaFisicaForm(request.POST, request.FILES, prefix="fisica")
            if form_perfil.is_valid() and request.recaptcha_is_valid:
                usuario_final = form_cadastro.save()
                endereco_final = form_endereco.save(commit=False)
                endereco_final.usuario = usuario_final
                endereco_final.save()
                perfil_final = form_perfil.save(commit=False)
                perfil_final.usuario = usuario_final
                perfil_final.save()
                return redirect(home)
            else:
                messages.add_message(request, messages.INFO, 'reCaptcha não preenchido.')
                messages.add_message(request, messages.INFO, form_perfil.errors)
        else:
            messages.add_message(request, messages.INFO, form_cadastro.errors)
            messages.add_message(request, messages.INFO, form_endereco.errors)
    formCadastro = CadastroForm(prefix="cadastro")
    formEndereco = EnderecoForm(prefix="endereco")
    formPF = PessoaFisicaForm(prefix="fisica")
    formPJ = PessoaJuridicaForm(prefix="juridica")
    return render(request, 'usuario/cadastro.html', {'form': formCadastro,
                                                     'formEndereco': formEndereco,
                                                     'formPF': formPF,
                                                     'formPJ': formPJ})

def esqueci_senha(request):
    if request.method == "POST":
        form_esqueci = PasswordResetForm(request.POST)
        if form_esqueci.is_valid():
            form_esqueci.save(subject_template_name="", email_template_name="usuario/email-esqueci.html", from_email="")
            messages.add_message(request, messages.INFO, 'Um e-mail com instruções para alteração de senha foi enviado.')
    form_esqueci = PasswordResetForm()
    return render(request, 'usuario/esqueci-senha.html', {'form_esqueci': form_esqueci})

def alterar_senha(request):
    if request.method == "POST":
        form_senha = SetPasswordForm(request.POST)
        if form_senha.is_valid():
            form_senha.save()
            messages.add_message(request, messages.INFO, 'Sua senha foi alterada com sucesso!')
            if request.user.is_authenticated:
                return redirect('perfil', request.user)
            else:
                messages.add_message(request, messages.INFO, 'Realize o login para continuar.')
                return redirect('home')
    form_senha = SetPasswordForm()
    return render(request, 'usuario/alterar-senha.html', {'form_senha': form_senha})