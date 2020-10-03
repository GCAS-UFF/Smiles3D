from .models import Pedido, UF_CHOICES
from django import forms
from localflavor.br.forms import BRZipCodeField
from django_starfield import Stars


class EnderecoEntregaForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('endereco_entrega', 'complemento_entrega', 'cep_entrega', 'cidade_entrega', 'uf_entrega')

    endereco_entrega = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '50'}),
        required=True
    )

    complemento_entrega = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '10'}),
        required=True
    )

    cep_entrega = BRZipCodeField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', "onblur": "pesquisacep(this.value);"}),
        required=True,
        max_length=9
    )

    cidade_entrega = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '15'}),
        required=True
    )

    uf_entrega = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=UF_CHOICES
    )

