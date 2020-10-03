from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Status
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import EnderecoEntregaForm
from perfil.models import Enderecos, Avaliacao
from perfil.forms import AvaliacaoForm
from oferta.models import Oferta
from pregao.models import Pregao

@login_required
def meusPedidos(request):
    lista_pedidos = Pedido.objects.filter(usuario=request.user).order_by('-data')
    paginator = Paginator(lista_pedidos, 10)
    page = request.GET.get('page')
    pedidos = paginator.get_page(page)
    return render(request, 'pedido/meus-pedidos.html', {"pedidos": pedidos})

@login_required
def pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if request.POST:
        form_avaliacao = AvaliacaoForm(request.POST)
        if form_avaliacao.is_valid():
            form_avaliacao.save()
            pedido.avaliacao_realizada = True;
            return render(request, 'pedido/pedido.html', {'pedido': pedido})
    form_avaliacao = AvaliacaoForm()
    return render(request, 'pedido/pedido.html', {'pedido': pedido,
                                                  'form_avaliacao': form_avaliacao})

@login_required
def novoPedido(request, slug_pregao, id_oferta):
    endereco_usuario = get_object_or_404(Enderecos, usuario=request.user)
    oferta_do_pedido = get_object_or_404(Oferta, id=id_oferta)
    pregao_do_pedido = get_object_or_404(Pregao, slug_pregao=slug_pregao)
    status = get_object_or_404(Status, id=1)
    if request.POST:
        form_endereco_entrega = EnderecoEntregaForm(request.POST)
        if form_endereco_entrega.is_valid():
            novo_pedido = form_endereco_entrega.save(commit=False)
            oferta_do_pedido.aceite = True
            novo_pedido.comprador = request.user
            novo_pedido.vendedor = oferta_do_pedido.usuario
            novo_pedido.oferta = oferta_do_pedido
            novo_pedido.forma_pagamento = oferta_do_pedido.forma_pagamento
            novo_pedido.forma_envio = oferta_do_pedido.forma_envio
            pregao_do_pedido.close = True
            novo_pedido.pregao = pregao_do_pedido
            novo_pedido.status = status;
            pedido_criado = novo_pedido.save()
            return redirect('pedido', pedido_criado.id)

        else:
            novo_pedido = Pedido.objects.create(vendedor=oferta_do_pedido.usuario, comprador=request.user, oferta=oferta_do_pedido, pregao=pregao_do_pedido,
                                                forma_pagamento=oferta_do_pedido.forma_pagamento, forma_envio=oferta_do_pedido.forma_envio, status=status,
                                                endereco_entrega=endereco_usuario.endereco, complemento_entrega=endereco_usuario.complemento, cep_entrega=endereco_usuario.cep,
                                                cidade_entrega=endereco_usuario.cidade, uf_entrega=endereco_usuario.uf)


            oferta_do_pedido.aceite = True
            pregao_do_pedido.close = True
            return redirect('pedido', novo_pedido.id)

    form_endereco_entrega = EnderecoEntregaForm()
    return render(request, 'pedido/novo-pedido.html', {'endereco_usuario': endereco_usuario,
                                                       'form_endereco_entrega': form_endereco_entrega,
                                                       'pregao': pregao_do_pedido,
                                                       'oferta': oferta_do_pedido})