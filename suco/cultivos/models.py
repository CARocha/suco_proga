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
    area = models.FloatField('Área')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cultivos de pastos"
        
class Componente(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class TipoCultivos(models.Model):
    tipo = models.ForeignKey(TipoCultivos)
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nombre
        
class Cultivos(models.Model):
    cultivo = models.ForeignKey(TipoCultivos, verbose_name="Cultivos")
    area = models.FloatField('Area Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    precio = models.FloatField('Precio de venta en el mercado local')
    venta_libre = models.ManyToManyField(AquienVende, verbose_name='Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año', choices=CHOICE_OPCION)
    
    class Meta:
        verbose_name_plural = "Cultivos en la Finca"
