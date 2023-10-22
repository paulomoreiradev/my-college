from django.db import models

class Disciplina(models.Model):
    TIPO_CHOICES = (
        ('E', 'Eletiva'),
        ('O', 'Obrigatória'),
        ('OP', 'Optativa'),
    )
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    creditos = models.IntegerField()
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    requisito = models.ManyToManyField("self")

    def __str__(self):
        return self.nome

class Semestre(models.Model):
    id = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    disciplinas = models.ManyToManyField(Disciplina)


class Curso(models.Model):
    TURNO_CHOICES = (
        ('D', 'Diurno'),
        ('N', 'Noturno'),
    )
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
    qtd_semestres = models.IntegerField()
    minimo_creditos_obrigatorias = models.IntegerField(default=1664)
    minimo_creditos_eletivas = models.IntegerField(default=448)
    minimo_creditos_optativas = models.IntegerField(default=1216)
    semestres = models.ManyToManyField(Semestre)

    def __str__(self):
        return self.codigo

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

class Conclusao(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas_concluidas = models.ManyToManyField(Disciplina)
