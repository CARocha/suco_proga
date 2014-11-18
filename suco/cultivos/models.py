# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from suco.animal_produccion.models import *
from django.core.cache import cache
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.

class Pastos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class CultivoPasto(models.Model):
    tipo = models.ForeignKey(Pastos, verbose_name="Tipo de pastos")
    area = models.FloatField('Área en manzana')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cultivos de pastos"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class division(models.Model):
    cuanto = models.FloatField('Cuantas divisiones de potrero hay')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Divisiones de potrero"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Componente(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class TipoCultivos(models.Model):
    tipo = models.ForeignKey(Componente)
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=20)
    conversion_kg = models.FloatField('Conversión a kilo (multiplicar con)', default=1)

    def __unicode__(self):
        return self.nombre+ " (Unidad : "+self.unidad+")"

    class Meta:
        verbose_name_plural = "Tipos cultivos en la finca"
        ordering = ('nombre',)
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Cultivos(models.Model):
    cultivo = models.ForeignKey(TipoCultivos, verbose_name="Cultivos")
    area = models.FloatField('Area Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    precio = models.FloatField('Precio de venta en el mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    def __unicode__(self):
        return self.cultivo.nombre+" (Unidad: "+self.cultivo.unidad+")"
    class Meta:
        verbose_name_plural = "Cultivos en la Finca"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class Patio(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Cultivos de patio"
        ordering = ('nombre',)
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class CultivosPatio(models.Model):
    cultivo = models.ForeignKey(Patio, verbose_name="Cultivos")
    area = models.CharField('Números de arboles', max_length=200)
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    precio = models.FloatField('Precio de venta en el mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cultivos en el patio"

    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

