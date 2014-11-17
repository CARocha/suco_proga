# -*- coding: UTF-8 -*-

from django.contrib import admin
from suco.caching.models import *

class CachingAdmin(admin.ModelAdmin):
    #desde octubre 2014, los jovenes estan vinculados con las encuestas, entonces no necesitamos nombre/edad/sexo/cedula no mas.
    #exclude = ('usuario', 'edad', 'sexo', 'cedula') #anadir 'nombre' despues de la importacion.. Simon.
    inlines = []
    #list_display = ('joven', 'nombre', 'fecha', 'formacion', 'comunidad', 'escolaridad','encuesta_numero')
    #list_filter = ['comunidad', 'formacion']
    #search_fields = ['joven__nombre', 'comunidad__nombre', 'formacion__nombre']
    #date_hierarchy = 'fecha'

#utility :P
admin.site.register(Caching, CachingAdmin)
