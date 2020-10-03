from django.urls import path
from .views import meusPedidos, pedido, novoPedido

urlpatterns = [
    path('meus-pedidos/', meusPedidos, name='meus-pedidos'),
    path('pedido/<int:id_pedido>', pedido, name='pedido'),
    path('novo-pedido/<slug:slug_pregao>/<int:id_oferta>', novoPedido, name='novo-pedido'),
]
