# Generated by Django 4.2.2 on 2023-08-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0027_locais_de_estagio_bairro_locais_de_estagio_cursos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidade',
            name='ativa',
            field=models.BooleanField(default=True),
        ),
    ]
