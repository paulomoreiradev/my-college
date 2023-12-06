from django.views.generic import FormView, TemplateView, DetailView
from django.shortcuts import redirect, render
from django.db import connection
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from app.forms import (AlunoForm, ObrigatoriasS1Form, ObrigatoriasS2Form,ObrigatoriasS3Form, ObrigatoriasS4Form,
 ObrigatoriasS6Form,ObrigatoriasS7DiurnoForm, ObrigatoriasS8DiurnoForm, ObrigatoriasS7NoturnoForm, ObrigatoriasS8NoturnoForm, ObrigatoriasS9NoturnoForm, Eletivas4Form, Eletivas5Form, OptativasForm
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

class ObrigatoriasDiurnoView(TemplateView):
    template_name = 'diurno/obrigatorias_diurno_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['semestre1_form'] = ObrigatoriasS1Form()
        context['semestre2_form'] = ObrigatoriasS2Form()
        context['semestre3_form'] = ObrigatoriasS3Form()
        context['semestre4_form'] = ObrigatoriasS4Form()
        context['semestre6_form'] = ObrigatoriasS6Form()
        context['semestre7noturno_form'] = ObrigatoriasS7NoturnoForm()
        context['semestre8noturno_form'] = ObrigatoriasS8NoturnoForm()
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
        ]

        aluno = Aluno.objects.first()
        disciplinas = Disciplina.objects.all()
        conclusao = Conclusao.objects.get(id=194)
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
            
        # conclusion = Conclusao.objects.create(aluno=aluno)
        # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
        conclusao.disciplinas_concluidas.set(disciplinas_concluidas)

        return HttpResponseRedirect(reverse('eletivas-diurno'))

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
        conclusao = Conclusao.objects.get(id=195)
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
            
        # conclusion = Conclusao.objects.create(aluno=aluno)
        # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
        conclusao.disciplinas_concluidas.set(disciplinas_concluidas)


        return HttpResponseRedirect(reverse('eletivas-noturno'))




class EletivasDiurnoView(TemplateView):
    template_name = "eletivas_diurno_form.html"

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
        conclusao = Conclusao.objects.get(id=194)
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
            
        # conclusion = Conclusao.objects.create(aluno=aluno)
        # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
        conclusao.disciplinas_concluidas.add(*disciplinas_concluidas)

        return HttpResponseRedirect(reverse('optativas-diurno'))
    
class EletivasNoturnoView(TemplateView):
    template_name = "eletivas_noturno_form.html"

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
        conclusao = Conclusao.objects.get(id=195)
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
            
        # conclusion = Conclusao.objects.create(aluno=aluno)
        # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
        conclusao.disciplinas_concluidas.add(*disciplinas_concluidas)

        return HttpResponseRedirect(reverse('optativas-noturno'))


class OptativasDiurnoView(FormView):
    form_class = OptativasForm
    success_url = reverse_lazy("resultado")
    template_name = "optativas_diurno_form.html"

    def form_valid(self, form):
        # Your form processing logic here

        # Set the success URL with a specific pk
        specific_pk = 194  # Replace with your specific pk or logic to determine it
        self.success_url = reverse_lazy('resultado', args=[specific_pk])

        return super().form_valid(form)
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            aluno = Aluno.objects.first()
            conclusao = Conclusao.objects.get(id=194)
            optativas = Disciplina.objects.all()
            disciplinas_concluidas = []
            for optativa in optativas:
                if optativa.tipo == "OP":
                    field_name = f'is_selected_{optativa.id}'
                    if form.cleaned_data.get(field_name, False):
                        disciplinas_concluidas.append(optativa)

            # conclusion = Conclusao.objects.create(aluno=aluno)
            # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
            conclusao.disciplinas_concluidas.add(*disciplinas_concluidas)
            return self.form_valid(form)

        else:
                return HttpResponse("404")
        
class OptativasNoturnoView(FormView):
    form_class = OptativasForm
    success_url = reverse_lazy("resultado")
    template_name = "optativas_noturno_form.html"

    def form_valid(self, form):
        # Your form processing logic here

        # Set the success URL with a specific pk
        specific_pk = 195  # Replace with your specific pk or logic to determine it
        self.success_url = reverse_lazy('resultado', args=[specific_pk])

        return super().form_valid(form)    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            aluno = Aluno.objects.first()
            conclusao = Conclusao.objects.get(id=195)
            optativas = Disciplina.objects.all()
            disciplinas_concluidas = []
            for optativa in optativas:
                if optativa.tipo == "OP":
                    field_name = f'is_selected_{optativa.id}'
                    if form.cleaned_data.get(field_name, False):
                        disciplinas_concluidas.append(optativa)

            # conclusion = Conclusao.objects.create(aluno=aluno)
            # conclusion.disciplinas_concluidas.set(disciplinas_concluidas)
            conclusao.disciplinas_concluidas.add(*disciplinas_concluidas)
            return self.form_valid(form)

        else:
                return HttpResponse("404")
        
class ConclusaoView(DetailView):
    model = Conclusao
    template_name = "app/conclusao.html"
    context_object_name = 'conclusao'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Define the total credits needed for graduation
        total_obrigatorias = 1664
        total_eletivas = 448
        total_optativas = 1216

        # Calculate the sum of credits for each type of Disciplina
        eletivas_sum = self.object.disciplinas_concluidas.filter(tipo='E').aggregate(Sum('creditos'))['creditos__sum'] or 0
        obrigatorias_sum = self.object.disciplinas_concluidas.filter(tipo='O').aggregate(Sum('creditos'))['creditos__sum'] or 0
        optativas_sum = self.object.disciplinas_concluidas.filter(tipo='OP').aggregate(Sum('creditos'))['creditos__sum'] or 0

        # Calculate the percentages
        eletivas_percentage = (eletivas_sum / total_eletivas) * 100 if total_eletivas > 0 else 0
        obrigatorias_percentage = (obrigatorias_sum / total_obrigatorias) * 100 if total_obrigatorias > 0 else 0
        optativas_percentage = (optativas_sum / total_optativas) * 100 if total_optativas > 0 else 0

        context['eletivas_sum'] = eletivas_sum
        context['obrigatorias_sum'] = obrigatorias_sum
        context['optativas_sum'] = optativas_sum

        context['eletivas_percentage'] = eletivas_percentage
        context['obrigatorias_percentage'] = obrigatorias_percentage
        context['optativas_percentage'] = optativas_percentage

        return context