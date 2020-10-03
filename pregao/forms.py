from .models import Pregao, n_dentes, Material, Comentario, EscalaCores
from django import forms

class PregaoForm(forms.ModelForm):
    class Meta:
        model = Pregao
        fields = ['id', 'dente', 'tipo', 'cor', 'escala', 'material', 'extra', 'preco', 'prazo', 'modeloSTL']

    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    dente = forms.MultipleChoiceField(
        error_messages={'required': 'Campo obrigatório'},
        choices=n_dentes,
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )

    tipo = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=True
    )

    cor = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=EscalaCores.objects.all().order_by('cor'),
        empty_label='--- Selecione uma cor  ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    escala = forms.CharField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=True
    )

    material = forms.ModelChoiceField(
      error_messages={'required': 'Campo obrigatório.', },
      queryset=Material.objects.all().order_by('m'),
      empty_label='--- Selecione um material  ---',
      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
      required=True
    )

    extra = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'maxlength': '500', 'rows': '10', 'cols': '40'}),
        required=False
    )

    preco = forms.DecimalField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'display: inline-block'}),
        required=True
    )

    prazo = forms.DateField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm text-inline'}),
        required=True
    )

    modeloSTL = forms.FileField(
        error_messages={'required': 'Campo obrigatório'},
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']

    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500', 'rows': '10', 'cols': '40'}),
        required=False
    )
