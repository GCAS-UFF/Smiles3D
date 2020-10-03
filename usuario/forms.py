from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'tipo']

    tipo = forms.ChoiceField(
        choices=(('Pessoa Jurídica', 'Pessoa Jurídica'),
                 ('Pessoa Física', 'Pessoa Física')),
        label="Cadastrar como",
        widget=forms.RadioSelect(attrs={"class":"cadastro-tipo"})
    )

    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Confirmação de Senha',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "A confirmação de senha não está correta",
                code='password_mismatch'
            )
        return password2

    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user