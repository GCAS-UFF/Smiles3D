from django.db import models
from pregao.models import Pregao
from django.utils.translation import ugettext_lazy as _
from oferta.models import Oferta, FormaPagamento, FormaEnvio
from usuario.models import CustomUser
import datetime

UF_CHOICES = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
)

class Status(models.Model):
    status = models.CharField(_('Status'), max_length=90)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Pedido(models.Model):
    vendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name='vendedor')
    comprador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name='comprador')
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, null=False, blank=False)
    pregao = models.ForeignKey(Pregao, on_delete=models.CASCADE, null=False, blank=False)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, null=False, blank=False)
    forma_envio = models.ForeignKey(FormaEnvio, on_delete=models.CASCADE, null=False, blank=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, null=False, blank=False)
    endereco_entrega = models.CharField(_('Endereço'), max_length=90)
    complemento_entrega = models.CharField(_('Complemento'), max_length=90)
    cep_entrega = models.CharField(_('CEP(somente números)'), max_length=10)
    cidade_entrega = models.CharField(_('Cidade'), max_length=20, default='')
    uf_entrega = models.CharField(_('UF'), max_length=2, choices=UF_CHOICES)
    data = models.DateField(default=datetime.date.today)
    avaliacao_realizada = models.BooleanField(default=False)



    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'