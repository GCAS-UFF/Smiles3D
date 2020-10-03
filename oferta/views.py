from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Oferta
from pregao.models import Pregao
from .forms import formOferta
from django.core.paginator import Paginator

@login_required
def visualizarOferta(request, slug_pregao, id_oferta):
    pregao = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    oferta = get_object_or_404(Oferta, pk=id_oferta)
    return render(request, 'oferta/oferta.html', {'oferta': oferta,
                                                     'pregao': pregao})

@login_required
def removerOferta(request, slug_pregao, id_oferta):
    oferta = get_object_or_404(Oferta, id=id_oferta)
    oferta.delete()
    return redirect('visualizar-pregao', slug_pregao)

@login_required
def editarOferta(request, slug_pregao, id_oferta):
    oferta = get_object_or_404(Oferta, id=id_oferta)
    if request.POST:
        form_oferta = formOferta(request.POST, request.FILES, instance=oferta)
        if form_oferta.is_valid():
            form_oferta.save()
            return redirect('visualizar-pregao', slug_pregao)
    else:
        form_negocio = formOferta(instance=oferta)
    pregao = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    return render(request, 'oferta/edita-oferta.html', {'pregao': pregao,
                                                        'form_oferta': form_oferta,
                                                        'id_oferta': id_oferta})

@login_required
def ofertasRecebidas(request):
    lista_ofertas = Oferta.objects.filter(dono_pregao=request.user, close=False).order_by('-data')
    paginator = Paginator(lista_ofertas, 10)
    page = request.GET.get('page')
    ofertas = paginator.get_page(page)
    return render(request, 'oferta/ofertas.html', {"ofertas": ofertas})

def rejeitarOferta(request, slug_pregao, id_oferta):
    oferta = get_object_or_404(Oferta, id=id_oferta)
    oferta.aceite = False
    return redirect('visualizar-pregao', slug_pregao)