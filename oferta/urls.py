from django.urls import path
from .views import visualizarOferta, removerOferta, editarOferta, ofertasRecebidas, rejeitarOferta

urlpatterns = [
    path('oferta/<slug:slug_pregao>/<int:id_oferta>', visualizarOferta, name='visualizar-oferta'),
    path('remove-oferta/<slug:slug_pregao>/<int:id_oferta>', removerOferta, name='remove-oferta'),
    path('edita-oferta/<slug:slug_pregao>/<int:id_oferta>', editarOferta, name='edita-oferta'),
    path('rejeitar-oferta/<slug:slug_pregao>/<int:id_oferta>', rejeitarOferta, name='rejeitar-oferta'),
    path('ofertas/', ofertasRecebidas, name="ofertas"),
]