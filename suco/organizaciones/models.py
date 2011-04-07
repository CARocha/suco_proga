# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *

# Create your models here.

class OrgGremiales(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones Gremiales"

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'),(3,'Ninguno'))
        
class OrganizacionGremial(models.Model):
    ''' 2. Organizacion Gremial
    '''
    socio = models.ManyToManyField(OrgGremiales,
                                   verbose_name="Es socio/a de una organización gremial")
    desde_socio = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Organización Gremial"
        
class OrgComunitarias(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones comunitarias"
        
class BeneficioOrgComunitaria(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Beneficios de estar organizado en comunidad"
        
class NoOrganizado(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Porque No esta organizado"
        
class OrganizacionComunitaria(models.Model):
    ''' 2.1 Organizacion comunitarias
    '''
    numero = models.IntegerField('¿Cuántas organizaciones están activas en la localidad o comunidad')
    pertence = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION)
    cual_organizacion = models.ManyToManyField(OrgComunitarias, verbose_name="¿A cuál organización comunitaria pertenece?")
    cual_beneficio = models.ManyToManyField(BeneficioOrgComunitaria, verbose_name="¿Cuáles son los beneficios de estar organizado")
    no_organizado = models.ManyToManyField(NoOrganizado, verbose_name="¿Porqué no esta organizado?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Organizacion Comunitaria"
