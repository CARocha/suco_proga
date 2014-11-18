from django.contrib import admin
from suco.jovenes.models import *

class JovenAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']

class GrupoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Grupo,GrupoAdmin)
admin.site.register(Joven, JovenAdmin)
