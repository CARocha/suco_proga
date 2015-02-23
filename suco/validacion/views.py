# Create your views here.
from __future__ import division

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.db import models
from suco.lugar.models import Centroregional
from suco.jovenes.models import Grupo

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



    return render(request, template, locals())