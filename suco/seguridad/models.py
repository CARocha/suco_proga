# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from django.core.cache import cache
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.
class Componentes(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Alimentos(models.Model):
    componete = models.ForeignKey(Componentes)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Alimentos"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Seguridad(models.Model):
    ''' Modelo Seguridad alimentaria
    '''
    alimento = models.ForeignKey(Alimentos)
    producen = models.IntegerField('Producen en la finca', choices=CHOICE_OPCION)
    compran = models.IntegerField('Compran para completar la necesidad', choices=CHOICE_OPCION)
    consumen = models.IntegerField('Consumen lo necesario en los meses de verano', choices=CHOICE_OPCION)
    consumen_invierno = models.IntegerField('Consumen lo necesario en los meses de invierno', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.alimento.nombre
    
    class Meta:
        verbose_name_plural = "Seguridad alimentaria"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

# Cuales son los riesgos que hace la finca vulnerable

class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        ordering = ('causa__nombre', 'nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Vulnerable(models.Model):
    ''' modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Casa cuanto hay daños graves en la finca?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cuáles son los riesgos que hacen la finca vulnerable"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

 #Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Riesgos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Gestión de riesgos"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")
