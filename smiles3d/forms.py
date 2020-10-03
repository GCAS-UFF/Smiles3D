from django import forms

class PesquisaForm(forms.Form):
   class Meta:
      fields = ('busca_por')

   busca_por = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120', 'placeholder': 'Pesquisar por...', 'style': 'border-radius: 0px;'}),
      required=False)

class ContatoForm(forms.Form):
   class Meta:
      fields = ('nome', 'email', 'assunto', 'mensagem')

   nome = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'maxlength': '120',
                                    'placeholder': 'Nome', 'style': 'border-radius: 0px;'}),
      required=False
   )

   email = forms.EmailField(
      widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm mb-2', 'maxlength': '120',
                                    'placeholder': 'E-mail', 'style': 'border-radius: 0px;'}),
      required=False
   )

   assunto = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'maxlength': '120',
                                    'placeholder': 'Assunto', 'style': 'border-radius: 0px;'}),
      required=False
   )

   mensagem = forms.CharField(
      widget=forms.Textarea(attrs={'class': 'form-control form-control-sm mb-2', 'maxlength': '120','placeholder': 'Mensagem', 'style': 'border-radius: 0px;'}),
      required=False
   )