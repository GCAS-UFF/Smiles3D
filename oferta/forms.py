from django import forms
from .models import Oferta, FormaEnvio, FormaPagamento
from pregao.models import Pregao

class formOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['preco', 'prazo', 'observacao', 'modeloSTL', 'forma_pagamento', 'forma_envio']

    preco = forms.DecimalField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    prazo = forms.DateField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    forma_pagamento = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=FormaPagamento.objects.all().order_by('forma_pagamento'),
        empty_label='--- Selecione uma forma de pagamento  ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    forma_envio = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=FormaEnvio.objects.all().order_by('forma_envio'),
        empty_label='--- Selecione uma forma de envio  ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    observacao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'maxlength': '500', 'rows': '10', 'cols': '40'}),
        required=False
    )

    modeloSTL = forms.FileField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        required=False
    )

class ChangeRegistro(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ()
        exclude = ('preco', 'prazo', 'observacao', 'registro', 'user', 'pregao', 'data', 'modeloSTL')
        cleaned_data = []

class ChangeClose(forms.ModelForm):
    class Meta:
        model = Pregao
        fields = ()
        exclude = ('tipo', 'dente', 'escala', 'cor', 'material', 'extra', 'close','data', 'preco','prazo','usuario','modeloSTL')
        cleaned_data = []

class RemoveNegocioForm(forms.Form):
    class Meta:
        fields = ('negocio_id',)

    negocio_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)