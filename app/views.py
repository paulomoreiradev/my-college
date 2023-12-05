from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect, render
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from app.forms import (AlunoForm, ObrigatoriasS1Form, ObrigatoriasS2Form,ObrigatoriasS3Form, ObrigatoriasS4Form,
 ObrigatoriasS6Form, ObrigatoriasS7NoturnoForm, ObrigatoriasS8NoturnoForm, ObrigatoriasS9NoturnoForm, Eletivas4Form, Eletivas5Form, OptativasForm
 )
from app.models import Semestre, Disciplina, Aluno, Conclusao
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

    semestre5 = Semestre.objects.get(id=5)
    disciplinas5 = semestre5.disciplinas.all()

    semestre6 = Semestre.objects.get(id=6)
    disciplinas6 = semestre6.disciplinas.all()

    semestre7_diurno = Semestre.objects.get(id=7)
    disciplinas7_diurno = semestre7_diurno.disciplinas.all()

    semestre8_diurno = Semestre.objects.get(id=8)
    disciplinas8_diurno = semestre8_diurno.disciplinas.all()

    semestre7_noturno = Semestre.objects.get(id=9)
    disciplinas7_noturno = semestre7_noturno.disciplinas.all()

    semestre8_noturno = Semestre.objects.get(id=10)
    disciplinas8_noturno = semestre8_noturno.disciplinas.all()

    semestre9_noturno = Semestre.objects.last()
    disciplinas9_noturno = semestre9_noturno.disciplinas.all()
    
    disciplinas = Disciplina.objects.all()

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
        'disciplinas': disciplinas,
        }
    
    # print(semestre1)
    # print(connection.queries)
    return render (request, "app/sobre-o-curso.html", context )

def trilhas(request):
    return render (request, "app/trilhas.html")

def o_projeto(request):
    return render(request, "app/sobre-o-projeto.html")

def calculadora_turno(request):
    return render(request, "app/calculadora-turno.html")

def obrigatorias_diurno (request):
    return render(request, "obrigatorias-diurno.html")

class ObrigatoriasNoturnoView(TemplateView):
    template_name = 'noturno/obrigatorias_noturno_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['semestre1_form'] = ObrigatoriasS1Form()
        context['semestre2_form'] = ObrigatoriasS2Form()
        context['semestre3_form'] = ObrigatoriasS3Form()
        context['semestre4_form'] = ObrigatoriasS4Form()
        context['semestre6_form'] = ObrigatoriasS6Form()
        context['semestre7noturno_form'] = ObrigatoriasS7NoturnoForm()
        context['semestre8noturno_form'] = ObrigatoriasS8NoturnoForm()
        context['semestre9noturno_form'] = ObrigatoriasS9NoturnoForm()
        return context
    
    def post(self, request, *args, **kwargs):
        semestres_form_classes = [
            ObrigatoriasS1Form,
            ObrigatoriasS2Form,
            ObrigatoriasS3Form,
            ObrigatoriasS4Form,
            ObrigatoriasS6Form,
            ObrigatoriasS7NoturnoForm,
            ObrigatoriasS8NoturnoForm,
            ObrigatoriasS9NoturnoForm,
        ]

        aluno = Aluno.objects.first()
        disciplinas = Disciplina.objects.all()
        disciplinas_concluidas = []

        for form_class in semestres_form_classes:
            form = form_class(request.POST)
            if form.is_valid():
                for disciplina in disciplinas:
                    if disciplina.tipo == "O":
                        field_name = f'is_selected_{disciplina.id}'
                        if form.cleaned_data.get(field_name, False):
                            disciplinas_concluidas.append(disciplina)
            else:
                raise Exception
            
        conclusion = Conclusao.objects.create(aluno=aluno)
        conclusion.disciplinas_concluidas.set(disciplinas_concluidas)

        return HttpResponseRedirect(reverse('eletivas'))




class EletivasView(TemplateView):
    template_name = "eletivas_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['eletivas4_form'] = Eletivas4Form()
        context['eletivas5_form'] = Eletivas5Form()
        return context
    
    def post(self, request, *args, **kwargs):

        eletivas_form_classes = [
            Eletivas4Form,
            Eletivas5Form,
        ]
        
        aluno = Aluno.objects.first()
        disciplinas = Disciplina.objects.all()
        disciplinas_concluidas = []
        
        for form_class in eletivas_form_classes:
            form = form_class(request.POST)
            if form.is_valid():
                for disciplina in disciplinas:
                    if disciplina.tipo == "E":
                        field_name = f'is_selected_{disciplina.id}'
                        if form.cleaned_data.get(field_name, False):
                            disciplinas_concluidas.append(disciplina)
            else:
                raise Exception
            
        conclusion = Conclusao.objects.create(aluno=aluno)
        conclusion.disciplinas_concluidas.set(disciplinas_concluidas)

        return HttpResponseRedirect(reverse('optativas'))


class OptativasView(FormView):
    form_class = OptativasForm
    success_url = reverse_lazy("index")
    template_name = "optativas_form.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            aluno = Aluno.objects.first()
            optativas = Disciplina.objects.all()
            disciplinas_concluidas = []
            for optativa in optativas:
                if optativa.tipo == "OP":
                    field_name = f'is_selected_{optativa.id}'
                    if form.cleaned_data.get(field_name, False):
                        disciplinas_concluidas.append(optativa)

            conclusion = Conclusao.objects.create(aluno=aluno)
            conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
            return self.form_valid(form)

        else:
                return HttpResponse("404")