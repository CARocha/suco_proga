# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from django.core.cache import cache
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.

class Acceso(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Parcela(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Solar(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre   

    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Documento(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
 
    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class AccesoTierra(models.Model):
    tierra = models.ForeignKey(Acceso, verbose_name="¿De quien es la tierra que usted va a trabajar")
    parcela = models.ForeignKey(Parcela, verbose_name="Parcela")
    casa = models.ForeignKey(Solar, verbose_name="¿De quien es la casa donde vive?")
    documento = models.ForeignKey(Documento, verbose_name="Documento legal de la propiedad, a nombre a quién")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Acceso a tierra y agua"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

# Uso de Tierra

class Uso(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso de tierra"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class UsoTierra(models.Model):
    ''' Uso de tierra
    '''
    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra")
    area = models.FloatField('Área en Mz')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.tierra.nombre
    class Meta:
        verbose_name_plural = "Uso del total de la finca"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

#Acceso al agua
class AguaAcceso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class AccesoAgua(models.Model):
    nombre = models.ManyToManyField(AguaAcceso, verbose_name="Tiene acceso a agua", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Tiene acceso a agua"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

#Existencia de arboles
        
class Maderable(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles maderables"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Forrajero(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles forrageros"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Energetico(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles energeticos"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Frutal(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles frutal"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class ExistenciaArboles(models.Model):
    ''' Existencia de arboles en la finca
        por tipo de uso
    '''
    maderable = models.ManyToManyField(Maderable, verbose_name="Maderable")
    cantidad_maderable = models.IntegerField()
    forrajero = models.ManyToManyField(Forrajero, verbose_name="Forrajero")
    cantidad_forrajero = models.IntegerField()
    energetico = models.ManyToManyField(Energetico, verbose_name="Energetico")
    cantidad_energetico = models.IntegerField()
    frutal = models.ManyToManyField(Frutal, verbose_name="Frutal")
    cantidad_frutal = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = " Existencia de Arboles"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

#Reforestacion

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades de reforestacion"
        ordering = ('nombre',)

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Reforestacion(models.Model):
    ''' reforestacion
    '''
    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
    cantidad = models.IntegerField('Cantidad de arboles sembrados')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.reforestacion.nombre
    
    class Meta:
        verbose_name_plural = "Reforestacion"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")
