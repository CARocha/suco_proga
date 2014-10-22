# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from suco.encuesta.models import *
from suco.jovenes.models import *
from suco.lugar.models import *
from suco.finca_tierra.models import *

CHOICE_SEXO = (('', u'Sexo'),(1,'Hombre'),(2,'Mujer')) #CUIDADO -> los informes viejas tenian 1 como Hombre et 2 como Mujer, et es el contrario.

CHOICE_SEXO_NUEVO = (('3', u'Los dos sexos'),('2','Solo hombres'),('1','Solo mujeres'))

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
    ('___', '--------- RESULTADO INTERMEDIO / Producción agrícola sostenible ----------'),
    ('aumento_de_la_produccion','% de aumento de la producción'),
    ('nivel_de_diversificacion_de_la_produccion', 'Nivel de diversificación de la producción'),
    ('parcelas_cultivadas_con_tecnicas_que_mejoran_el_ecosistema', '%  de parcelas cultivadas con técnicas que mejoran el ecosistema '),
    ('___', '--------- RESULTADO INTERMEDIO / Acceso mejorado a  la cantidad y calidad de alimentos durante todo el año ----------'),
    ('no_meses_acceso_variedad_alimentos', 'Nº de meses en los que la mayoría de familias tienen acceso a una variedad de alimentos '),
    ('familias_acceso_alimentos_todo_ano', '% de familias participantes del proyecto que tienen acceso a una gama de diversos alimentos durante todo el año '),
    ('___', '--------- RESULTADO INTERMEDIO / Ingresos provenientes de actividades de transformación y comercialización, de las y los jóvenes productores de Las Segovias aumentados  ----------'),
    ('aumento_ingresos_de_transformacion_y_comercializacion', '% de aumento de los ingresos provenientes de las actividades de transformación y comercialización '),
    ('familias_con_ingresos_de_comercializacion_y_transformacion', 'Nº de familias que obtienen ingresos provenientes de la comercialización y la transformación de la producción'),
    ('___', '--------- RESULTADO INTERMEDIO / Autonomía y capacidad de influencia aumentada de las jóvenes mujeres productoras de Las Segovias, a nivel individual y comunitario ----------'),
    ('nivel_aceptacion_mujeres', 'Nivel de aceptación de la opinión de las jóvenes mujeres en la toma de decisión en el seno de las parcelas agrícolas familiares '),
    ('mujeres_actividades_agricolas_parcela', '%  de jóvenes mujeres que participan en las actividades agrícolas de la parcela familiar'),
    ('mujeres_actividades_cumunitarias', '% de jóvenes mujeres que participan en actividades comunitarias '),
    ('hombres_actividades_habitualmente_mujer', '% de jóvenes hombres que participan en actividades habitualmente reservadas a las mujeres'),
    ('___','---------RESULTADO ULTIMO------------'),
    ('ultime_familias_superandoi_minimo', 'Nº de familias superando el mínimo de subsistencia en términos de producción agrícola'),
    ('ultime_aumento_ingresos', '% de aumento de los ingresos proviniendo de la producción agrícola'),
    ('ultime_nivel_satisfaccion_condiciones', 'Nivel de satisfacción de las condiciones de vida asociadas a la producción agrícola y alimentaria '),
    ('ultime_percepcion_condiciones_medioambiente', 'Percepción de las condiciones del medioambiente (riqueza de los suelos, disponibilidad de agua) '),
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
    informe_tipo = forms.ChoiceField(choices = CHOICE_INFORME_TIPO, required=True,  widget=forms.Select(attrs={'class': 'form-control', 'style': 'max-width:200px'}))

    #Informes originales
    fecha = forms.ChoiceField(choices=get_anios(), label="Años", widget=forms.Select(attrs={'class': 'form-control'}))
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Departamento", widget=forms.Select(attrs={'class': 'form-control'}))
    municipio = forms.CharField(widget = forms.Select(attrs={'class': 'form-control'}), required=False)
    comunidad = forms.CharField(widget = forms.Select(attrs={'class': 'form-control'}), required=False)
    sexo = forms.ChoiceField(choices = CHOICE_SEXO, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    dueno = forms.ModelChoiceField(queryset=Documento.objects.all(), 
            required=False, empty_label="Dueños", widget = forms.Select(attrs={'class': 'form-control'}))
#    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False, initial=u"Dueño")

    #Nuevos informes - Octubre 2014
    grupo = forms.ModelMultipleChoiceField(queryset=Grupo.objects.all(), required=False)
    centroregional = forms.ModelMultipleChoiceField(queryset=Centroregional.objects.all(), required=False)
    numero_encuesta = forms.ChoiceField(choices = CHOICE_ENCUESTA_NUM, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    indicador = forms.ChoiceField(choices = CHOICE_INFORME_INDICADOR, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    solo_jovenes_con_dos = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)
    sexo_encuesta = forms.ChoiceField(choices = CHOICE_SEXO_NUEVO, required=False, widget=forms.Select(attrs={'class': 'form-control'}))






