# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from suco.animal_produccion.models import *

# Create your models here.

class Pastos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class CultivoPasto(models.Model):
    tipo = models.ForeignKey(Pastos, verbose_name="Tipo de pastos")
    area = models.FloatField('Área en manzana')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cultivos de pastos"
        
class division(models.Model):
    cuanto = models.FloatField('Cuantas divisiones de potrero hay')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Divisiones de potrero"
        
class Componente(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class TipoCultivos(models.Model):
    tipo = models.ForeignKey(Componente)
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos cultivos en la finca"
        
class Cultivos(models.Model):
    cultivo = models.ForeignKey(TipoCultivos, verbose_name="Cultivos")
    area = models.FloatField('Area Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    precio = models.FloatField('Precio de venta en el mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cultivos en la Finca"
        
class Patio(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
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
    
