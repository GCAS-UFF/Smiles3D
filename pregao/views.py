from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import PregaoForm, ComentarioForm
from .models import Pregao, Comentario
from oferta.models import Oferta
from oferta.forms import formOferta
from django.contrib import messages

@login_required
def novoPregao(request):
    if request.POST:
        id = request.POST.get('id')
        if id:
            pregao = get_object_or_404(Pregao, pk=id)
            form = PregaoForm(request.POST, request.FILES, instance=pregao)
        else:
            form = PregaoForm(request.POST, request.FILES)
        if form.is_valid():
            pregao = form.save(commit=False)
            if not id:
                pregao.usuario = request.user
                pregao.slug_pregao = slugify(pregao.tipo + request.user.username + str(pregao.data))
            form.save()
            return redirect('visualizar-pregao', pregao.slug_pregao)
    else:
        form = PregaoForm()
    return render(request, 'pregao/novo-pregao.html', {'form': form})

@login_required
def verPregao(request, slug_pregao):
    pregao = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    comentarios = Comentario.objects.filter(pregao=pregao)
    ofertas = Oferta.objects.filter(pregao=pregao)
    if request.method == 'POST':
        if 'oferta' in request.POST:
            formoferta = formOferta(request.POST, request.FILES)
            if formoferta.is_valid():
                offer = formoferta.save(commit=False)
                offer.pregao = pregao
                offer.usuario = request.user
                offer.save()
                messages.add_message(request, messages.INFO, 'Oferta criada com sucesso!')
        elif 'comentario' in request.POST:
            formcomment = ComentarioForm(request.POST)
            if formcomment.is_valid():
                comment = formcomment.save(commit=False)
                comment.pregao = pregao
                comment.user = request.user
                comment.save()
                messages.add_message(request, messages.INFO, 'Comentário criado com sucesso!')
    form_comentario = ComentarioForm()
    form_oferta = formOferta()
    return render(request, 'pregao/pregao.html', {'form_oferta': form_oferta,
                                                  'form_comment': form_comentario,
                                                  'pregao': pregao,
                                                  'comentarios': comentarios,
                                                  'ofertas': ofertas})

@login_required
def meusPregoes(request):
    lista_pregoes = Pregao.objects.filter(usuario=request.user).order_by('-data')
    paginator = Paginator(lista_pregoes, 10)
    page = request.GET.get('page')
    pregoes = paginator.get_page(page)
    return render(request, 'pregao/meus-pregoes.html', {"pregoes": pregoes})

@login_required
def meusPregoesAbertos(request):
    lista_pregoes = Pregao.objects.filter(usuario=request.user, close=False).order_by('-data')
    paginator = Paginator(lista_pregoes, 10)
    page = request.GET.get('page')
    pregoes = paginator.get_page(page)
    return render(request, 'pregao/lista-pregoes.html', {"pregoes": pregoes})

@login_required()
def meusPregoesFechados(request):
    lista_pregoes = Pregao.objects.filter(usuario=request.user, close=True).order_by('-data')
    paginator = Paginator(lista_pregoes, 10)
    page = request.GET.get('page')
    pregoes = paginator.get_page(page)
    return render(request, 'pregao/meus-pregoes.html', {"pregoes": pregoes})

@login_required
def todosAbertos(request):
    lista_pregoes = Pregao.objects.filter(close=False).order_by('-data')
    paginator = Paginator(lista_pregoes, 10)
    page = request.GET.get('page')
    pregoes = paginator.get_page(page)
    return render(request, 'pregao/lista-pregoes.html', {"pregoes": pregoes})

@login_required
def editaPregao(request, slug_pregao):
    pregao = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    form = PregaoForm(instance=pregao)
    form.fields['id'].initial = pregao.id
    return render(request, 'pregao/novo-pregao.html', {'form': form})

@login_required
def deletePregao(request, slug_pregao):
    pregao = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    ofertas = Oferta.objects.filter(pregao=pregao)
    if ofertas:
        for oferta in ofertas:
            oferta.delete()
    comentarios = Comentario.objects.filter(pregao=pregao)
    if comentarios:
        for comentario in comentarios:
            comentario.delete()
    pregao.delete()
    messages.add_message(request, messages.INFO, 'Pregão excluído com sucesso!')
    return redirect('meus-pregoes')

def deleteComentario(request, slug_pregao, id_comentario):
    comentario = get_object_or_404(Comentario, pk=id_comentario)
    comentario.delete()
    messages.add_message(request, messages.INFO, 'Comentário excluído com sucesso!')
    return redirect('visualizar-pregao', slug_pregao)
