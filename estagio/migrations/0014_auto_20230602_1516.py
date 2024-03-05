# Generated by Django 3.2.15 on 2023-06-02 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
        ('estagio', '0013_auto_20230530_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='vaga',
        ),
        migrations.AddField(
            model_name='supervisor',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa'),
        ),
        migrations.RemoveField(
            model_name='vagas',
            name='curso',
        ),
        migrations.AddField(
            model_name='vagas',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estagio.curso'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='vagas',
            name='secretaria',
        ),
        migrations.AddField(
            model_name='vagas',
            name='secretaria',
            field=models.ManyToManyField(to='estagio.Secretaria'),
        ),
        migrations.CreateModel(
            name='Vaga_Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estagio.vagas')),
            ],
        ),
    ]