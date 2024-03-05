# Generated by Django 3.2.17 on 2023-02-14 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissão', models.CharField(max_length=150, null=True, verbose_name='Profissão')),
                ('escolaridade', models.CharField(blank=True, choices=[('efi', 'Ensino Fundamental Incompleto'), ('efc', 'Ensino Fundamental Completo'), ('emi', 'Ensino Médio Incompleto'), ('emc', 'Ensino Médio Completo'), ('ct', 'Curso Técnico'), ('esi', 'Ensino Superior Incompleto'), ('esc', 'Ensino Superior Completo')], max_length=3, null=True, verbose_name='Escolaridade')),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro(a)'), ('c', 'Casado(a)'), ('s', 'Separado(a)'), ('d', 'Divorciado(a)'), ('v', 'Viúvo(a)')], max_length=1, null=True, verbose_name='Estado Civil')),
                ('aceita_mais_informacoes', models.BooleanField(null=True, verbose_name='Declaro que aceito receber email com as informações das atividades')),
                ('li_e_aceito_termos', models.BooleanField(null=True, verbose_name='Li e aceito os termos')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, null=True)),
                ('pessoa', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['dt_inclusao'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sigla', models.CharField(max_length=3, unique=True)),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horária')),
                ('descricao', models.TextField(default='')),
                ('ativo', models.BooleanField(default=True)),
                ('nivel_ensino', models.CharField(choices=[('F', 'Ensino Fundamental'), ('M', 'Ensino Médio'), ('T', 'Ensino Técnico'), ('S', 'Ensino Superior')], max_length=1)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sigla', models.CharField(max_length=6, unique=True)),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do Instrutor')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('endereco', models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço')),
                ('bairro', models.CharField(blank=True, max_length=80, null=True)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Instrutor',
                'verbose_name_plural': 'Instrutores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Justificativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=256, null=True)),
                ('motivo', models.CharField(choices=[('a', 'Ausência'), ('d', 'Desmatricula')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do local')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=80, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'locais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=128, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_permitido', models.IntegerField(verbose_name='Quantidade de alunos permitidos')),
                ('idade_minima', models.IntegerField(blank=True, null=True, verbose_name='Idade mínima')),
                ('idade_maxima', models.IntegerField(blank=True, null=True, verbose_name='Idade máxima')),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pre', 'Pré-inscrição'), ('agu', 'Aguardando'), ('ati', 'Ativa'), ('acc', 'Ativa e aceitando candidatos'), ('enc', 'Encerrada')], default='pre', max_length=3, verbose_name='Qual o status da turma?')),
                ('grupo_whatsapp', models.URLField(blank=True, null=True, verbose_name='Link do grupo do Whatsapp')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso', verbose_name='Atividade')),
                ('instrutores', models.ManyToManyField(to='cursos.Instrutor', verbose_name='Instrutor(es)')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.local')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ['curso', 'local'],
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('1', 'Domingo'), ('2', 'Segunda-Feira'), ('3', 'Terça-Feira'), ('4', 'Quarta-Feira'), ('5', 'Quinta-Feira'), ('6', 'Sexta-Feira'), ('7', 'Sábado')], max_length=1)),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'ordering': ['dia_semana', 'horario_inicio', 'horario_fim'],
            },
        ),
        migrations.CreateModel(
            name='Turno_estabelecido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.turma')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.turno')),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='turnos',
            field=models.ManyToManyField(through='cursos.Turno_estabelecido', to='cursos.Turno'),
        ),
        migrations.AddField(
            model_name='turma',
            name='user_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TurmaUserInclusao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turma',
            name='user_ultima_alteracao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TurmaUserAlteracao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do responsável')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular p/ contato do responsável')),
                ('email', models.EmailField(max_length=254, verbose_name='Email p/ contato do responsável')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Qual foi o sexo atribuído no seu nascimento?')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=150, null=True, verbose_name='Endereço do responsável')),
                ('bairro', models.CharField(max_length=80, null=True, verbose_name='Bairro')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('profissao', models.CharField(max_length=150, verbose_name='Profissão')),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro(a)'), ('c', 'Casado(a)'), ('s', 'Separado(a)'), ('d', 'Divorciado(a)'), ('v', 'Viúvo(a)')], max_length=1, verbose_name='Estado Civil')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('matricula', models.CharField(editable=False, max_length=16, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('c', 'Candidato'), ('s', 'Selecionado'), ('a', 'Aluno'), ('e', 'Desistente'), ('d', 'Desmatriculado'), ('f', 'Formado'), ('r', 'Realocado')], default='c', max_length=1)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.turma')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
                'ordering': ['-dt_inclusao'],
                'get_latest_by': 'dt_inclusao',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.instituicao'),
        ),
        migrations.AddField(
            model_name='curso',
            name='requisitos',
            field=models.ManyToManyField(to='cursos.Requisito'),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CursoUserInclusao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_ultima_alteracao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CursoUserAlteracao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_aula', models.DateField(verbose_name='Data da aula')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=256, verbose_name='Descrição')),
                ('associacao_turma_turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.turno_estabelecido')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['-dt_aula'],
                'unique_together': {('dt_aula', 'associacao_turma_turno')},
            },
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Presente'), ('a', 'Ausente'), ('c', 'Saiu mais cedo')], max_length=1)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.aula')),
                ('justificativa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cursos.justificativa')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.matricula')),
            ],
            options={
                'verbose_name': 'Presença',
                'verbose_name_plural': 'Presenças',
                'ordering': ['-dt_inclusao'],
                'unique_together': {('aula', 'matricula')},
            },
        ),
    ]