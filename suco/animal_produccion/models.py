# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from django.core.cache import cache
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
# Create your models here.

class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Animales-Finca"
        ordering = ('nombre',)
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class ProductoAnimal(models.Model):
    animal = models.ForeignKey(Animales)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    def __unicode__(self):
        return '%s - %s' % (self.animal.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Finca - Producto"
        ordering = ('animal__nombre', 'nombre',)
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")


class AnimalesFinca(models.Model):
    ''' Modelo animales en la finca
    '''
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField('Cantidad de animales')
    valor = models.FloatField('Valor unitario')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.animales.nombre
    
    class Meta:
        verbose_name_plural = "Animales de la finca"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")


class AquienVende(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")

class ProduccionConsumo(models.Model):
    producto = models.ForeignKey(ProductoAnimal)
    total_produccion = models.FloatField('Total producion por año')
    consumo = models.FloatField('Consumo familiar por año')
    precio = models.FloatField('Precio unitario de venta actual en mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Producción y consumo en la finca"
    def clear_cache(sender, **kwargs):
        cache.clear()
    post_save.connect(clear_cache, dispatch_uid="clear_cache_postsave")
    post_delete.connect(clear_cache, dispatch_uid="clear_cache_postdelete")