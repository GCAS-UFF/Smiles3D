# Generated by Django 2.0 on 2020-08-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(verbose_name='Avaliação')),
                ('extra', models.TextField(blank=True, max_length=500, null=True, verbose_name='Comentários')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=90, verbose_name='Endereço')),
                ('complemento', models.CharField(max_length=90, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP(somente números)')),
                ('cidade', models.CharField(default='', max_length=20, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome completo')),
                ('media_avaliacao', models.IntegerField(default=0, verbose_name='Avaliação')),
                ('profissao', models.CharField(choices=[('Dentista', 'Dentista'), ('Protético', 'Protético'), ('Outra', 'Outra')], max_length=10, verbose_name='*Profissão')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='*CPF(somente números)')),
                ('cro', models.CharField(max_length=25, unique=True, verbose_name='*CRO(somente números)')),
                ('autonomo', models.BooleanField(verbose_name='Autônomo')),
                ('telefone', models.CharField(max_length=12, verbose_name='*Telefone(somente números)')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='FotosUsuarios')),
            ],
            options={
                'verbose_name': 'Cadastro de Pessoa Física',
                'verbose_name_plural': 'Cadastros de Pessoas Físicas',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=30, unique=True, verbose_name='*Razão social')),
                ('departamento', models.CharField(choices=[('Laboratório Protético', 'Laboratório Protético'), ('Clínica Odontológica', 'Clínica Odontológica'), ('Outro tipo', 'Outro tipo')], max_length=100, verbose_name='Estabelecimento')),
                ('cnpj', models.CharField(max_length=14, unique=True, verbose_name='CNPJ(somente números)')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone (somente números)')),
                ('media_avaliacao', models.IntegerField(default=0.0, verbose_name='Avaliação')),
                ('funcionarios', models.IntegerField(default=0, verbose_name='Funcionários')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='FotosUsuarios')),
            ],
            options={
                'verbose_name': 'Cadastro de Pessoa Jurídica',
                'verbose_name_plural': 'Cadastros de Pessoas Jurídicas',
            },
        ),
    ]
