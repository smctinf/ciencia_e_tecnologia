# Generated by Django 4.1.7 on 2023-02-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_instituicao_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipo_carga_horaria',
            field=models.CharField(choices=[('h', 'Hora'), ('m', 'Minuto')], default='h', max_length=1),
            preserve_default=False,
        ),
    ]
