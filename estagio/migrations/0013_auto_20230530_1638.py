# Generated by Django 3.2.15 on 2023-05-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0012_alter_estudante_vaga_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome curso'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='matricula',
            field=models.CharField(max_length=50, verbose_name='Matricula'),
        ),
        migrations.AlterField(
            model_name='estudante_vaga',
            name='data_fim',
            field=models.DateField(blank=True, null=True, verbose_name='Data termino'),
        ),
        migrations.AlterField(
            model_name='estudante_vaga',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data inicio'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='local',
            field=models.CharField(max_length=200, verbose_name='Local Secretaria'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome secretaria'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome supervisor'),
        ),
        migrations.AlterField(
            model_name='universidade',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome universidade'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome vagas'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='quantidade_de_vagas',
            field=models.IntegerField(verbose_name='Quantidade de vagas'),
        ),
    ]
