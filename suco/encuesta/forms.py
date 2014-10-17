# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from suco.encuesta.models import *
from suco.jovenes.models import *
from suco.lugar.models import *
from suco.finca_tierra.models import *

CHOICE_SEXO = (('', u'Sexo'),(1,'Hombre'),(2,'Mujer')) #CUIDADO -> los informes viejas tenian 1 como Hombre et 2 como Mujer, et es el contrario.

CHOICE_ENCUESTA_NUM = (
    ('1','Primera encuesta'),
    ('2','Segunda encuesta'),
    ('3','Comparar las dos encuestas'),
    )
CHOICE_INFORME_TIPO = (
    ('','Qué tipo de informes?'),
    ('informes_originales','Informes originales'),
    ('informes_nuevos','Nuevos informes'),
    )
CHOICE_INFORME_INDICADOR = (
    ('aumento_de_la_produccion','% de aumento de la producción'),
    )

def get_anios():
    choices = []
    years = []
    for en in Encuesta.objects.all().order_by('fecha'):
        years.append(en.fecha.year)
    for year in list(set(years)):
        choices.append((year, year))
    return choices

#El formulario original ariba
class MonitoreoForm(forms.Form):

    #escojer entre tipos de informes (originales y nuevos)
    informe_tipo = forms.ChoiceField(choices = CHOICE_INFORME_TIPO, required=True)

    #Informes originales
    fecha = forms.ChoiceField(choices=get_anios(), label="Años")
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Departamento")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comunidad = forms.CharField(widget = forms.Select, required=False)
    sexo = forms.ChoiceField(choices = CHOICE_SEXO, required=False)
    dueno = forms.ModelChoiceField(queryset=Documento.objects.all(), 
            required=False, empty_label="Dueños")
#    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False, initial=u"Dueño")

    #Nuevos informes - Octubre 2014
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(),
            required=False, empty_label="Todos los grupos")

    numero_encuesta = forms.ChoiceField(choices = CHOICE_ENCUESTA_NUM, required=True)
    indicador = forms.ChoiceField(choices = CHOICE_INFORME_INDICADOR, required=True)
    jovenes_activados_solo = forms.BooleanField(required=False)




