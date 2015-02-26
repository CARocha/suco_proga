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
import json
import collections
from django.contrib.auth.decorators import login_required

@login_required
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
                    joven.total_cultivo_area1_triple = uso.area * 3
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
                    joven.total_cultivo_area2_triple = uso.area * 3
            #Area total de cultivos - SUMA de cada cultivo
            joven.area_cultivos2 = encuesta2.aggregate(area=Sum('cultivos__area'))['area']
            if joven.area_cultivos2 > (joven.total_cultivo_area2 * 3):
                joven.demasadio_cultivos_vs_uso2 = "bug"

        joven.cultivos_in_encuesta = collections.OrderedDict()
        for tipocultivo in TipoCultivos.objects.all().order_by('nombre'):
            joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)] = collections.OrderedDict()
            try:
                qs = Cultivos.objects.filter(encuesta=encuesta1,cultivo=tipocultivo)
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'] = qs[0]
            except:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'] = None
            try:
                qs=Cultivos.objects.filter(encuesta=encuesta2,cultivo=tipocultivo)
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'] = qs[0]
            except:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'] = None

            #KG por hectare
            if joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'] is not None:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].converted_kg = joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].cultivo.conversion_kg * joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].total
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].kg_por_manzana = joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].converted_kg / joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc1'].area
            if joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'] is not None:
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].converted_kg = joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].cultivo.conversion_kg * joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].total
                joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].kg_por_manzana = joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].converted_kg / joven.cultivos_in_encuesta[slugify(tipocultivo.nombre)]['enc2'].area




    return render(request, template, locals())



def validacion_save_joven_comment (request):
    jovenid = request.POST.get('jovenid')
    comment = request.POST.get('comment')

    try:
        joven = Joven.objects.get(id=jovenid)
        joven.validacion_datos_comentario_centro = comment
        joven.save()
    except:
        response_data = {}
        response_data['msg'] = 'error'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    response_data = {}
    response_data['msg'] = 'ok'
    return HttpResponse(json.dumps(response_data), content_type="application/json")