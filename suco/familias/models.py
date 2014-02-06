# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *

# Create your models here.

CHOICE_EDUCACION = ((1,'Mujeres entre 16 y 30 años'),
                    (2,'Hombres entre 16 y 30 años')
                   )
                   
CHOICE_SALUD = ((1,'Si'),
                (2,'No'),
                (3,'No sabe')
               )
                   
class Educacion(models.Model):
    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
    total = models.IntegerField('Número total')
    no_leer = models.IntegerField('No sabe leer y escribir')
    p_incompleta = models.IntegerField('Primaria incompleta')
    p_completa = models.IntegerField('Primaria completa')
    s_incompleta = models.IntegerField('Secundaria incompleta')
    bachiller = models.IntegerField()
    universitario = models.IntegerField()
    f_comunidad = models.IntegerField('Viven fuera de la comunidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()
        
    class Meta:
        verbose_name_plural = "Educacion"
        
class Salud(models.Model):
    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
    b_salud = models.IntegerField('# tiene buena salud')
    s_delicada = models.IntegerField('# tiene salud delicada')
    e_cronica = models.IntegerField('# tiene enfermedad crónica')
    v_centro = models.IntegerField('Visita centro de salud', choices=CHOICE_SALUD)
    v_medico = models.IntegerField('Visita médico privado', choices=CHOICE_SALUD)
    v_naturista = models.IntegerField('Visita médico naturista', choices=CHOICE_SALUD)
    automedica = models.IntegerField('Auto-medica', choices=CHOICE_SALUD)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()
        
    class Meta:
        verbose_name_plural = "Salud"
        
class PreguntaEnergia(models.Model):
    pregunta = models.CharField(max_length=200)

    def __unicode__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural = "Pregunta sobre energia"
        
class Cocinar(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Energia(models.Model):
    pregunta = models.ForeignKey(PreguntaEnergia)
    respuesta = models.IntegerField(choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        ordering = ('pregunta',)
        verbose_name_plural = "Energia"
        
class QueUtiliza(models.Model):
    cocina = models.ManyToManyField(Cocinar)
    encuesta = models.ForeignKey(Encuesta)

class FuenteConsumo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class TrataAgua(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class DisponibilidadAgua(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    
class AguaConsumo(models.Model):
    fuente = models.ManyToManyField(FuenteConsumo, verbose_name="Fuente de consumo de agua")
    tratar = models.ManyToManyField(TrataAgua, verbose_name="Como se trata el agua de beber y cocinar")
    disponible = models.ManyToManyField(DisponibilidadAgua, verbose_name="Disponibilidad de agua para uso domestico")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Agua para consumo humano"
        
class FuenteProduccion(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre    
    
class EquipoBombeo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
    
class EnergiaUtiliza(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre    
    
    
class AguaProduccion(models.Model):
    fuente = models.ManyToManyField(FuenteProduccion, verbose_name="Fuente de agua")
    equipo = models.ManyToManyField(EquipoBombeo, verbose_name="Equipo utilizado para bombeo")
    energia = models.ManyToManyField(EnergiaUtiliza, verbose_name="Energia Utilizada")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Agua para la producción"
