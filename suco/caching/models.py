# -*- coding: UTF-8 -*-

from django.db import models

#Permite de activar or desactivar el caching
class Caching(models.Model):
    activado  = models.BooleanField(default=0)
    def __unicode__(self):
            return 'Parametros del caching'
    class Meta:
        verbose_name_plural = "Parametros del caching"