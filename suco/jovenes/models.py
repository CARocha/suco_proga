# -*- coding: UTF-8 -*-
from django.db import models
from suco.lugar.models import *
from django.core.cache import cache
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.

CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no
CHOICE_SEXO = ( (1,'Hombre'),
                (2,'Mujer')
              )
CHOICE_ACTIVO = (
    (0, "No activo"),
    (1, "Activo en SUCO")
)

class Grupo(models.Model):
    nombre = models.CharField('Nombre del grupo', max_length=200)
    def __unicode__(self):
        return self.nombre

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Joven(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    cedula = models.CharField('Cedula', max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    grupo = models.ForeignKey(Grupo)
    idseguimiento = models.IntegerField()
    centroregional = models.ForeignKey(Centroregional)
    activo = models.IntegerField(choices=CHOICE_ACTIVO, verbose_name=u'Activo?', default=1)
    validacion_datos_comentario_direccion = models.TextField(default="", blank=True, verbose_name=u'Preguntas de la dirección, errores potenciales en los datos')
    validacion_datos_comentario_centro = models.TextField(default="", blank=True, verbose_name=u'Respuesta y explicaciones de los datos por el equipo regional')
    def __unicode__(self):
        return self.nombre+ " - "+self.grupo.nombre

    class Meta:
        verbose_name_plural = "Jovenes"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")
