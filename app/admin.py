from django.contrib import admin

from app.models import Aluno, Conclusao, Curso, Disciplina, Semestre

admin.site.register([
    Disciplina,
    Semestre,
    Curso,
    Aluno,
    Conclusao,
])
