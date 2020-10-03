# Generated by Django 2.0 on 2020-08-20 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oferta', '0001_initial'),
        ('pregao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='dono_pregao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oferta',
            name='pregao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pregao.Pregao'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='criador', to=settings.AUTH_USER_MODEL),
        ),
    ]
