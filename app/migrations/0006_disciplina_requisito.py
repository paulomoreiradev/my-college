# Generated by Django 4.2.6 on 2023-10-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_curso_minimo_creditos_optativas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='requisito',
            field=models.ManyToManyField(to='app.disciplina'),
        ),
    ]
