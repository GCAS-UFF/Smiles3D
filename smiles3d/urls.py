from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import home, sobre, pesquisa
from usuario.urls import urlpatterns as usuario_urls
from perfil.urls import urlpatterns as perfil_urls
from pregao.urls import urlpatterns as pregao_urls
from oferta.urls import urlpatterns as oferta_urls
from pedido.urls import urlpatterns as pedido_urls
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('logout/', logout, {'next_page': 'home'}, name="logout"),
    path('', include(usuario_urls)),
    path('', include(perfil_urls)),
    path('', include(pregao_urls)),
    path('', include(oferta_urls)),
    path('', include(pedido_urls)),
    path('login/', login, {'template_name': 'usuario/login.html'}, name='login'),
    path('sobre/', sobre, name='sobre'),
    path('busca/', pesquisa, name='pesquisar'),
    url(r'^captcha/', include('captcha.urls')),
]
