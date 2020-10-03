from django.core import validators
import re
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('E-mail'), max_length=100, unique=True)
    username = models.CharField(_('Nome de Usuário'), max_length=15, unique=True, validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), "O nome de usuário só pode conter letras, dígitos e o caracter _")])
    tipo = models.CharField(_('Tipo de Conta'), max_length=15)
    date_joined = models.DateTimeField(_('Data da Criação'), auto_now_add=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff_property(self):
        return self.is_admin
