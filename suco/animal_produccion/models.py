# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *

# Create your models here.

class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Animales-Finca"

class ProductoAnimal(models.Model):
    animal = models.ForeignKey(Animales)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s-%s' % (self.animales.nombre - self.nombre)

    class Meta:
        verbose_name_plural = "Finca - Producto"


class AnimalesFinca(models.Model):
    ''' Modelo animales en la finca
    '''
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField('Cantidad de animales')
    valor = models.FloatField('Valor')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.animales.nombre
    
    class Meta:
        verbose_name_plural = "Animales de la finca"

class AquienVende(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class ProduccionConsumo(models.Model):
    producto = models.ForeignKey(ProductoAnimal)
    total_produccion = models.IntegerField('Total producion por año')
    consumo = models.FloatField('Consumo familiar por año')
    precio = models.FloatField('Precio de venta actual en mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Producción y consumo en la finca"
