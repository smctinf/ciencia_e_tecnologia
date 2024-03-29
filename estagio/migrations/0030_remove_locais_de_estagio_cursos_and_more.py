# Generated by Django 4.2.2 on 2023-08-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0029_alter_universidade_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locais_de_estagio',
            name='cursos',
        ),
        migrations.AddField(
            model_name='estudante_vaga',
            name='matricula',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Matricula'),
        ),
        migrations.AddField(
            model_name='estudante_vaga',
            name='universidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='estagio.universidade'),
        ),
        migrations.RemoveField(
            model_name='vagas',
            name='curso',
        ),
        migrations.AddField(
            model_name='vagas',
            name='curso',
            field=models.ManyToManyField(to='estagio.curso'),
        ),
    ]
