# Generated by Django 4.2.6 on 2023-10-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_conclusao'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='minimo_creditos_optativas',
            field=models.IntegerField(default=1216),
        ),
        migrations.AlterField(
            model_name='curso',
            name='minimo_creditos_eletivas',
            field=models.IntegerField(default=448),
        ),
        migrations.AlterField(
            model_name='curso',
            name='minimo_creditos_obrigatorias',
            field=models.IntegerField(default=1664),
        ),
        migrations.AlterField(
            model_name='curso',
            name='semestres',
            field=models.ManyToManyField(to='app.semestre'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='tipo',
            field=models.CharField(choices=[('E', 'Eletiva'), ('O', 'Obrigatória'), ('OP', 'Optativa')], max_length=2),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='disciplinas',
            field=models.ManyToManyField(to='app.disciplina'),
        ),
    ]
