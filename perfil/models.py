from django.db import models
from django.utils.translation import ugettext_lazy as _
from usuario.models import CustomUser

DEPARTAMENTO_CHOICES = (
        ('Laboratório Protético', 'Laboratório Protético'),
        ('Clínica Odontológica', 'Clínica Odontológica'),
        ('Outro tipo', 'Outro tipo'),
    )

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

PROFISSAO_CHOICES = (
        ('Dentista', 'Dentista'),
        ('Protético', 'Protético'),
        ('Outra', 'Outra'),
    )


class PessoaJuridica(models.Model):
    razao_social = models.CharField(_('*Razão social'), max_length=30, unique=True)
    departamento = models.CharField(_('Estabelecimento'), max_length=100, choices=DEPARTAMENTO_CHOICES)
    cnpj = models.CharField(_('CNPJ(somente números)'), max_length=14, unique=True)
    telefone = models.CharField(_('Telefone (somente números)'), max_length=12)
    media_avaliacao = models.IntegerField(_("Avaliação"), default=0.0)
    funcionarios = models.IntegerField(_('Funcionários'), default=0)
    foto = models.ImageField(upload_to='FotosUsuarios', null=True, blank=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Cadastro de Pessoa Jurídica'
        verbose_name_plural = "Cadastros de Pessoas Jurídicas"


class PessoaFisica(models.Model):
    nome = models.CharField(_('Nome completo'), max_length=30)
    media_avaliacao = models.IntegerField(_("Avaliação"), default=0)
    profissao = models.CharField(_('*Profissão'), max_length=10, choices=PROFISSAO_CHOICES)
    cpf = models.CharField(_('*CPF(somente números)'), max_length=11, unique=True)
    cro = models.CharField(_('*CRO(somente números)'), max_length=25, unique=True)
    autonomo = models.BooleanField(_('Autônomo'), null=False, blank=False)
    empresa = models.ForeignKey(PessoaJuridica, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.CharField(_('*Telefone(somente números)'), max_length=12)
    foto = models.ImageField(upload_to='FotosUsuarios', null=True, blank=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Cadastro de Pessoa Física'
        verbose_name_plural = "Cadastros de Pessoas Físicas"


class Enderecos(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    endereco = models.CharField(_('Endereço'), max_length=90)
    complemento = models.CharField(_('Complemento'), max_length=90)
    cep = models.CharField(_('CEP(somente números)'), max_length=10)
    cidade = models.CharField(_('Cidade'), max_length=20, default='')
    uf = models.CharField(_('UF'), max_length=2, choices=UF_CHOICES)


class Avaliacao(models.Model):
    nota = models.IntegerField(_('Avaliação'))
    extra = models.TextField(_('Comentários'), max_length=500, null=True, blank=True)
    avaliador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="avaliador")
    avaliado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'