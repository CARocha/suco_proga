# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from suco.encuesta.models import *
from suco.lugar.models import *
from suco.finca_tierra.models import *

CHOICE_SEXO = (('', u'Sexo'),(1,'Hombre'),(2,'Mujer'))

def get_anios():
    choices = []
    years = []
    for en in Encuesta.objects.all().order_by('fecha'):
        years.append(en.fecha.year)
    for year in list(set(years)):
        choices.append((year, year))
    return choices

class MonitoreoForm(forms.Form):
    fecha = forms.ChoiceField(choices=get_anios(), label="Años")
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Departamento")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comunidad = forms.CharField(widget = forms.Select, required=False)
    sexo = forms.ChoiceField(choices = CHOICE_SEXO, required=False)
    dueno = forms.ModelChoiceField(queryset=Documento.objects.all(), 
            required=False, empty_label="Dueños")
#    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False, initial=u"Dueño")
