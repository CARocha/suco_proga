# Create your views here.
from __future__ import division

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.db import models
from suco.lugar.models import Centroregional
from suco.jovenes.models import Grupo
from suco.encuesta.views import get_encuestas
from suco.jovenes.models import *
from suco.encuesta.models import *
from suco.cultivos.models import *
from django.db.models import Sum, Count, Avg
from django.template.defaultfilters import slugify

import collections

def validacion (request, template="validacion/validacion.html"):

    centros = Centroregional.objects.all()

    return render(request, template, locals())

def validacion_centrochosen (request, centroid, template="validacion/validacion_centrochosen.html"):
    centro = Centroregional.objects.get(id=centroid)
    grupos = Grupo.objects.all()

    return render(request, template, locals())

def validacion_jovenlist (request, centroid, grupoid, template="validacion/validacion_jovenlist.html"):
    centro = Centroregional.objects.get(id=centroid)
    grupo = Grupo.objects.get(id=grupoid)

    jovenes = Joven.objects.filter(centroregional=centro, activo=1, grupo=grupo)
    for joven in jovenes:
        joven.all_encuestas1 = Encuesta.objects.filter(joven=joven, encuesta_numero=1, activado=True)
        joven.all_encuestas2 = Encuesta.objects.filter(joven=joven, encuesta_numero=2, activado=True)

        #default
        joven.encuesta1 = None
        joven.encuesta1_msg = ""
        joven.encuesta2 = None
        joven.encuesta2_msg = ""

        #recupera las 1ra y 2nda encuestas
        encuesta1 = Encuesta.objects.filter(joven=joven, encuesta_numero=1, activado=True)
        if encuesta1.count() > 1:
            joven.encuesta1_msg = "Hay mas que una primera encuesta para este joven. Por favor verificar y desactivar las encuestas no validas."
            joven.encuesta1 = "multiple"
        else:
            try:
                joven.encuesta1 = encuesta1[0]
            except:
                joven.encuesta1 = None

        encuesta2 = Encuesta.objects.filter(joven=joven, encuesta_numero=2, activado=True)
        if encuesta2.count() > 1:
            joven.encuesta2_msg = "Hay mas que una secunda encuesta para este joven. Por favor verificar y desactivar las encuestas no validas."
            joven.encuesta2 = "multiple"
        else:
            try:
                joven.encuesta2 = encuesta2[0]
            except:
                joven.encuesta2 = None

        #Area total de cultivos - USO de la tierra
        joven.total_cultivo_area1 = 0.0
        joven.demasadio_cultivos_vs_uso1 = False
        if joven.encuesta1 is not None and joven.encuesta1 != "multiple":
            for uso in joven.encuesta1.usotierra_set.all():
                if uso.tierra.id == 4:
                    joven.total_cultivo_area1 = uso.area
            #Area total de cultivos - SUMA de cada cultivo
            joven.area_cultivos1 = encuesta1.aggregate(area=Sum('cultivos__area'))['area']
            if joven.area_cultivos1 > (joven.total_cultivo_area1 * 3):
                joven.demasadio_cultivos_vs_uso1 = "bug"

        joven.total_cultivo_area2 = 0.0
        joven.demasadio_cultivos_vs_uso2 = False
        if joven.encuesta2 is not None and joven.encuesta2 != "multiple":
            for uso in joven.encuesta2.usotierra_set.all():
                if uso.tierra.id == 4:
                    joven.total_cultivo_area2 = uso.area
            #Area total de cultivos - SUMA de cada cultivo
            joven.area_cultivos2 = encuesta2.aggregate(area=Sum('cultivos__area'))['area']
            if joven.area_cultivos2 > (joven.total_cultivo_area2 * 3):
                joven.demasadio_cultivos_vs_uso2 = "bug"

        joven.cultivos_in_encuesta = collections.OrderedDict()
        for tipocultivo in TipoCultivos.objects.all().order_by('nombre'):
            joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)] = collections.OrderedDict()
            try:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'] = Cultivos.objects.filter(encuesta=encuesta1,cultivo=tipocultivo)[0]
            except:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'] = None
            try:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'] = Cultivos.objects.filter(encuesta=encuesta2,cultivo=tipocultivo)[0]
            except:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'] = None





    return render(request, template, locals())

def validacion_verifyjoven (request, centroid, grupoid, jovenid, template="validacion/validacion_verifyjoven.html"):
    centro = Centroregional.objects.get(id=centroid)
    grupo = Grupo.objects.get(id=grupoid)
    joven = Joven.objects.get(id=jovenid)
    query1 = Encuesta.objects.filter(joven=joven, encuesta_numero=1, activado=True)
    query2 = Encuesta.objects.filter(joven=joven, encuesta_numero=2, activado=True)

    errors = collections.OrderedDict()

    #Tipos de error
    errors['mismo_num_de_encuestas'] = [True, '']
    errors['uso_global_enc1']  = [True, '']
    errors['uso_global_enc2']  = [True, '']

    #Numero de encuestas 1 VS encuestas 2. Solo debe ser 1.
    num_encuesta1 = query1.count()
    num_encuesta2 = query2.count()

    encuesta1 = query1[0]
    encuesta2 = query2[0]

    #Area total de cultivos - USO de la tierra
    encuesta1.total_cultivo_area = 0.0
    for uso in encuesta1.usotierra_set.all():
        if uso.tierra.id == 4:
            encuesta1.total_cultivo_area = uso.area


    encuesta2.total_cultivo_area = 0.0
    for uso in encuesta2.usotierra_set.all():
        if uso.tierra.id == 4:
            encuesta2.total_cultivo_area = uso.area

    #Area total de cultivos - SUMA de cada cultivo
    encuesta1.area_cultivos = query1.aggregate(area=Sum('cultivos__area'))['area']
    encuesta2.area_cultivos = query2.aggregate(area=Sum('cultivos__area'))['area']

    if (encuesta1.total_cultivo_area * 3) < encuesta1.area_cultivos:
        errors['uso_global_enc1']  = [False, 'Areas de cultivos no se pueden.']
    if (encuesta2.total_cultivo_area * 3) < encuesta2.area_cultivos:
        errors['uso_global_enc1']  = [False, 'Areas de cultivos no se pueden.']

    #Detalaes de cada cultivo
    cultivos = TipoCultivos.objects.all().order_by('nombre')


    return render(request, template, locals())