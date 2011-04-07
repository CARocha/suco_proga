# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *


# Create your models here.
class Componentes(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Alimentos(models.Model):
    componete = models.ForeignKey(Componentes)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Alimentos"

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
        
# Cuales son los riesgos que hace la finca vulnerable

class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"
        
class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        
class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"
        
class Vulnerable(models.Model):
    ''' modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Casa cuanto hay daños graves en la finca?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Cuáles son los riesgos que hacen la finca vulnerable"
        
 #Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"

class Riesgos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Gestión de riesgos"
