from django.shortcuts import render
from django.db import connection
from app.models import Semestre, Disciplina

def index(request):    
    return render(request, "app/index.html")

def sobre(request):
    semestre1 = Semestre.objects.first()
    disciplinas1 = semestre1.disciplinas.all()

    semestre2 = Semestre.objects.get(id=2)
    disciplinas2 = semestre2.disciplinas.all()

    semestre3 = Semestre.objects.get(id=3)
    disciplinas3 = semestre3.disciplinas.all()

    semestre4 = Semestre.objects.get(id=4)
    disciplinas4 = semestre4.disciplinas.all()

    semestre5 = Semestre.objects.get(id=11)
    disciplinas5 = semestre5.disciplinas.all()

    semestre6 = Semestre.objects.get(id=5)
    disciplinas6 = semestre6.disciplinas.all()

    semestre7_diurno = Semestre.objects.get(id=6)
    disciplinas7_diurno = semestre7_diurno.disciplinas.all()

    semestre8_diurno = Semestre.objects.get(id=7)
    disciplinas8_diurno = semestre8_diurno.disciplinas.all()

    semestre7_noturno = Semestre.objects.get(id=8)
    disciplinas7_noturno = semestre7_noturno.disciplinas.all()

    semestre8_noturno = Semestre.objects.get(id=9)
    disciplinas8_noturno = semestre8_noturno.disciplinas.all()

    semestre9_noturno = Semestre.objects.get(id=10)
    disciplinas9_noturno = semestre9_noturno.disciplinas.all()

    context = {
        'disciplinas1': disciplinas1, 
        'disciplinas2': disciplinas2,
        'disciplinas3': disciplinas3,
        'disciplinas4': disciplinas4,
        'disciplinas5': disciplinas5,
        'disciplinas6': disciplinas6,
        'disciplinas7_diurno': disciplinas7_diurno,
        'disciplinas8_diurno': disciplinas8_diurno,
        'disciplinas7_noturno': disciplinas7_noturno,
        'disciplinas8_noturno': disciplinas8_noturno,
        'disciplinas9_noturno': disciplinas9_noturno,
        }
    
    # print(semestre1)
    # print(connection.queries)
    return render (request, "sobre.html", context )

def trilhas(request):
    return render (request, "trilhas.html")

