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
        #default
        joven.encuesta1 = None
        joven.encuesta1_msg = ""
        joven.encuesta2 = None
        joven.encuesta2_msg = ""

        #recupera las 1ra y 2nda encuestas
        encuesta1 = Encuesta.objects.filter(joven=joven, encuesta_numero=1, activado=True)
        if encuesta1.count() > 1:
            joven.encuesta1_msg = "Hay mas que una primera encuesta para este joven. Por favor verificar."
        else:
            try:
                joven.encuesta1 = encuesta1[0]
            except:
                pass

        encuesta2 = Encuesta.objects.filter(joven=joven, encuesta_numero=2, activado=True)
        if encuesta2.count() > 1:
            joven.encuesta2_msg = "Hay mas que una secunda encuesta para este joven. Por favor verificar."
        else:
            try:
                joven.encuesta2 = encuesta2[0]
            except:
                pass

    return render(request, template, locals())

def validacion_verifyjoven (request, centroid, grupoid, jovenid, template="validacion/validacion_verifyjoven.html"):
    centro = Centroregional.objects.get(id=centroid)
    grupo = Grupo.objects.get(id=grupoid)
    joven = Joven.objects.get(id=jovenid)
    encuesta1 = Encuesta.objects.filter(joven=joven, encuesta_numero=1, activado=True)[0]
    encuesta2 = Encuesta.objects.filter(joven=joven, encuesta_numero=2, activado=True)[0]



    return render(request, template, locals())