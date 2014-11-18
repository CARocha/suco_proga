# -*- coding: UTF-8 -*-

from django.contrib import admin
from suco.caching.models import *

class CachingAdmin(admin.ModelAdmin):
    inlines = []

#utility
admin.site.register(Caching, CachingAdmin)
