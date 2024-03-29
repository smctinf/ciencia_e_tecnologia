# Generated by Django 3.2.15 on 2023-11-29 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0033_remove_estudante_vaga_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='universidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.universidade', verbose_name='Sua universidade atual'),
        ),
        migrations.AlterField(
            model_name='historico_processo',
            name='status',
            field=models.CharField(choices=[('0', 'Aguardando liberação de vaga'), ('1', 'Lista de espera'), ('2', 'Aguardando reenvio do TCE'), ('3', 'Aguardando termo assinado pelas partes'), ('4', 'Processo de seleção concluída'), ('5', 'Estágio concluído')], default=0, max_length=1, verbose_name='Status'),
        ),
    ]
