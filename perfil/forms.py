from .models import PessoaJuridica, PessoaFisica, Enderecos, Avaliacao, UF_CHOICES, DEPARTAMENTO_CHOICES, PROFISSAO_CHOICES
from django import forms
from localflavor.br.forms import BRCNPJField, BRCPFField, BRZipCodeField
from django_starfield import Stars

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ('nome', 'cpf', 'cro', 'foto', 'profissao', 'autonomo', 'empresa', 'telefone')

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '30'}),
        required=True
    )

    cpf = BRCPFField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '11', 'data-mask':"000.000.000-00"}),
        required=True,
        max_length=14
    )

    cro = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '25'}),
        required=True
    )

    foto = forms.ImageField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        required=False
    )

    profissao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=PROFISSAO_CHOICES
    )

    autonomo = forms.ChoiceField(
        choices=[(True, 'Sim'), (False, 'Não')],
        widget=forms.RadioSelect(attrs={"class":"eh-autonomo"})
    )

    empresa = forms.ModelChoiceField(
        queryset=PessoaJuridica.objects.all().order_by('razao_social'),
        empty_label='--- Selecione uma empresa  ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False
    )

    telefone = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '11'}),
        required=True
    )


class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = ('razao_social', 'cnpj', 'foto', 'departamento', 'telefone')

    razao_social = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '30'}),
        required=True
    )

    cnpj = BRCNPJField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'data-mask':"00.000.000/0000-00"}),
        required=True,
        min_length=16
    )

    foto = forms.ImageField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        required=False
    )

    departamento = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=DEPARTAMENTO_CHOICES
    )

    telefone = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '11'}),
        required=True
    )


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Enderecos
        fields = ('endereco', 'complemento', 'cep', 'cidade', 'uf')

    endereco = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '50'}),
        required=True
    )

    complemento = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '10'}),
        required=True
    )

    cep = BRZipCodeField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', "onblur": "pesquisacep(this.value);"}),
        required=True,
        max_length=9
    )

    cidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '15'}),
        required=True
    )

    uf = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=UF_CHOICES
    )

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'extra']

    nota = forms.IntegerField(
        widget=Stars,
        error_messages={'required': 'Campo obrigatório'},
        required=True
    )

    extra = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'maxlength': '500', 'rows': '5'}),
        required=False
    )