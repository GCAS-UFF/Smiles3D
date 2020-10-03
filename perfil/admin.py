from django.contrib import admin
from .models import Enderecos, PessoaJuridica, PessoaFisica, Avaliacao

admin.site.register(Enderecos)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Avaliacao)
