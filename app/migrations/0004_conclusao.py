# Generated by Django 4.2.6 on 2023-10-17 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_curso_turno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aluno')),
                ('disciplinas_concluidas', models.ManyToManyField(to='app.disciplina')),
            ],
        ),
    ]
