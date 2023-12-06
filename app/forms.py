from django import forms
from django.views.generic import FormView
from app.models import Semestre, Aluno, Disciplina

class AlunoForm (forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ObrigatoriasS1Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre1 = Semestre.objects.first()
        disciplinas1 = semestre1.disciplinas.all()
        super(ObrigatoriasS1Form, self).__init__(*args, **kwargs)

        for obj in disciplinas1:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS2Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre2 = Semestre.objects.get(id=2)
        disciplinas2 = semestre2.disciplinas.all()
        super(ObrigatoriasS2Form, self).__init__(*args, **kwargs)

        for obj in disciplinas2:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS3Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre3 = Semestre.objects.get(id=3)
        disciplinas3 = semestre3.disciplinas.all()
        super(ObrigatoriasS3Form, self).__init__(*args, **kwargs)

        for obj in disciplinas3:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS4Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre4 = Semestre.objects.get(id=4)
        disciplinas4 = semestre4.disciplinas.all()
        super(ObrigatoriasS4Form, self).__init__(*args, **kwargs)

        for obj in disciplinas4:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS6Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre6 = Semestre.objects.get(id=6)
        disciplinas6 = semestre6.disciplinas.all()
        super(ObrigatoriasS6Form, self).__init__(*args, **kwargs)

        for obj in disciplinas6:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS7DiurnoForm:
    def __init__(self, *args, **kwargs):
        semestre7_diurno = Semestre.objects.get(id=7)
        disciplinas7_diurno = semestre7_diurno.disciplinas.all()
        super(ObrigatoriasS7DiurnoForm, self).__init__(*args, **kwargs)

        for obj in disciplinas7_diurno:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS8DiurnoForm:
    def __init__(self, *args, **kwargs):
        semestre8_diurno = Semestre.objects.get(id=8)
        disciplinas8_diurno = semestre8_diurno.disciplinas.all()
        super(ObrigatoriasS8DiurnoForm, self).__init__(*args, **kwargs)

        for obj in disciplinas8_diurno:
            if obj.tipo == 'O' and not obj.nome == 'ATIVIDADES COMPLEMENTARES':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS7NoturnoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre7_noturno = Semestre.objects.get(id=9)
        disciplinas7_noturno = semestre7_noturno.disciplinas.all()
        super(ObrigatoriasS7NoturnoForm, self).__init__(*args, **kwargs)

        for obj in disciplinas7_noturno:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS8NoturnoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre8_noturno = Semestre.objects.get(id=10)
        disciplinas8_noturno = semestre8_noturno.disciplinas.all()
        super(ObrigatoriasS8NoturnoForm, self).__init__(*args, **kwargs)

        for obj in disciplinas8_noturno:
            if obj.tipo == 'O':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class ObrigatoriasS9NoturnoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre9_noturno = Semestre.objects.get(id=11)
        disciplinas9_noturno = semestre9_noturno.disciplinas.all()
        super(ObrigatoriasS9NoturnoForm, self).__init__(*args, **kwargs)

        for obj in disciplinas9_noturno:
            if obj.tipo == 'O' and not obj.nome == 'ATIVIDADES COMPLEMENTARES':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )


class Eletivas4Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre4 = Semestre.objects.get(id=4)
        eletivas4 = semestre4.disciplinas.all()
        super(Eletivas4Form, self).__init__(*args, **kwargs)

        for obj in eletivas4:
            if obj.tipo == 'E':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )


class Eletivas5Form(forms.Form):
    def __init__(self, *args, **kwargs):
        semestre5 = Semestre.objects.get(id=5)
        eletivas5 = semestre5.disciplinas.all()
        super(Eletivas5Form, self).__init__(*args, **kwargs)

        for obj in eletivas5:
            if obj.tipo == 'E':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class OptativasForm(forms.Form):
    def __init__(self, *args, **kwargs):
        queryset = Disciplina.objects.all()
        super(OptativasForm, self).__init__(*args, **kwargs)

        for obj in queryset:
            if obj.tipo == 'OP':
                field_name = f'is_selected_{obj.id}'
                self.fields[field_name] = forms.BooleanField(
                    label=obj.nome,  # Replace with the actual field you want to display
                    initial=obj.is_selected if hasattr(obj, 'is_selected') else False,
                    required=False
                )

class HorasComplementaresForm(forms.Form):
    ...