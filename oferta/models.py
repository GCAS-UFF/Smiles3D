from django.db import models
from pregao.models import Pregao
from django.utils.translation import ugettext_lazy as _
import datetime
from usuario.models import CustomUser

class FormaPagamento(models.Model):
    forma_pagamento = models.TextField(_('Forma de Pagamento'), default='', null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'

    def __str__(self):
        return self.forma_pagamento

    def __unicode__(self):
        return self.forma_pagamento

class FormaEnvio(models.Model):
    forma_envio = models.TextField(_('Forma de Envio'), default='', null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = 'Forma de Envio'
        verbose_name_plural = 'Formas de Envio'

    def __str__(self):
        return self.forma_envio

    def __unicode__(self):
        return self.forma_envio

class Oferta(models.Model):
    preco = models.DecimalField(_('Preço'), default="0.00", max_digits=7, decimal_places=2)
    prazo = models.DateField(_('Prazo'), default=datetime.datetime.today)
    data = models.DateField(default=datetime.datetime.today)
    registro = models.BooleanField(default=False)
    observacao = models.TextField(_('Observações'), default='', null=True, blank=True,max_length=500)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="criador")
    dono_pregao = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="receptor")
    pregao = models.ForeignKey(Pregao, on_delete=models.CASCADE, null=True, blank=True)
    modeloSTL = models.FileField(_('Arquivo STL'), upload_to='media/STLFiles', blank=True, null=True)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, null=True, blank=True)
    forma_envio = models.ForeignKey(FormaEnvio, on_delete=models.CASCADE, null=True, blank=True)
    aceite = models.NullBooleanField(_('Oferta Aceitada'),blank=True, null=True)

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'


