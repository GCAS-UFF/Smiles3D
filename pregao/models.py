from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from multiselectfield import MultiSelectField
from usuario.models import CustomUser

materiais_choices = (
    ('Resina acrílica sobre estrutura em metal', 'Resina acrílica sobre estrutura em metal'),
    ('Resina composta sobre estrutura em zircônia', 'Resina composta sobre estrutura em zircônia'),
    ('Porcelana sobre estrutura em metal', 'Porcelana sobre estrutura em metal'),
    ('Porcelana sobre estrutura em zircônia', 'Porcelana sobre estrutura em zircônia'),
    ('Zircônia pura', 'Zircônia pura'),
)

n_dentes = (
    ('18', '18'),
    ('17', '17'),
    ('16', '16'),
    ('15', '15'),
    ('14', '14'),
    ('13', '13'),
    ('12', '12'),
    ('11', '11'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('48', '48'),
    ('47', '47'),
    ('46', '46'),
    ('45', '45'),
    ('44', '44'),
    ('43', '43'),
    ('42', '42'),
    ('41', '41'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),

)

class Material(models.Model):
    m = models.CharField(_('Material'), max_length=100, default='', primary_key=True)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.m

    def __unicode__(self):
        return self.m

class EscalaCores(models.Model):
    cor = models.CharField(_('Cor'), max_length=5, default='', primary_key=True)

    class Meta:
        verbose_name = 'Escala de Cor'
        verbose_name_plural = 'Escala de Cores'

    def __str__(self):
        return self.cor

    def __unicode__(self):
        return self.cor

class Pregao(models.Model):
    tipo = models.CharField(_('Tipo de serviço'), max_length=100, default='')
    dente = MultiSelectField(_('Dente'), choices=n_dentes,  default=' ', max_length=100)
    cor = models.ForeignKey(EscalaCores, on_delete=models.DO_NOTHING, default='')
    escala = models.CharField(_('Escala'), max_length=100, default=' ', null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING, default='')
    extra = models.TextField(_('Observações'), max_length=500, null=True, blank=True)
    close = models.BooleanField(default=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(default=datetime.date.today)
    preco = models.DecimalField(_('Preço'), default="0,00", max_digits=7, decimal_places=2)
    prazo = models.DateField(_('Prazo'), default=datetime.date.today)
    modeloSTL = models.FileField(_('Arquivo STL'), upload_to='STLFiles', blank=True, null=True)
    slug_pregao = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Pregão'
        verbose_name_plural = 'Pregões'

class Comentario(models.Model):
    comentario = models.TextField(_('Comentário'), max_length=500, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    pregao = models.ForeignKey('pregao', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'


