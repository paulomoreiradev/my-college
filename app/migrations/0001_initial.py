# Generated by Django 4.2.6 on 2023-10-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('creditos', models.IntegerField()),
                ('tipo', models.CharField(choices=[('E', 'Eletiva'), ('O', 'Obrigatória')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('disciplinas', models.ManyToManyField(to='app.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('turno', models.CharField(max_length=10)),
                ('qtd_semestres', models.IntegerField()),
                ('minimo_creditos_obrigatorias', models.IntegerField()),
                ('minimo_creditos_eletivas', models.IntegerField()),
                ('semestres', models.ManyToManyField(to='app.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
        ),
    ]