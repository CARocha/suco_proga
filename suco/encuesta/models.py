# -*- coding: UTF-8 -*-

from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.core.cache import cache
from suco.lugar.models import *
from suco.jovenes.models import *
from django.contrib.auth.models import User
import datetime
from suco.smart_selects.db_fields import ChainedForeignKey 


# Create your models here.
class Recolector(models.Model):
    ''' Esta es la clase para el nombre del recolector
    '''
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Recolector"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")


class Escolaridad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Escolaridad"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")


class Tecnica(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Formación técnica"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class ParticipacionProyecto(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")


CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no

CHOICE_SEXO = ( (1,'Hombre'),
                (2,'Mujer')
              )

CHOICE_ENCUESTA_NUMERO = (
    (1,'Primera encuesta'),
    (2,'Segunda encuesta'),
    (3,'Por determinar'),
    )

class Encuesta(models.Model):
    ''' Esta es la parte de la encuesta donde van los demas
    '''
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    nombre = models.CharField('Nombre (vieja manera)', max_length=200)
    cedula = models.CharField('Cedula (vieja manera)', max_length=200, null=True, blank=True)
    edad = models.IntegerField()
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    enquesta_numero = models.IntegerField(choices=CHOICE_ENCUESTA_NUMERO,default=3)
    joven = models.ForeignKey(Joven,null=True)
    escolaridad = models.ForeignKey(Escolaridad)
    formacion = models.ForeignKey(Tecnica)
    participacion = models.ManyToManyField(ParticipacionProyecto)
    finca = models.CharField('Nombre de Finca', max_length=200)
    municipio = models.ForeignKey(Municipio)
    comunidad = ChainedForeignKey(
        Comunidad, 
        chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False, 
        auto_choose=True
                        )
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Encuestas"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")