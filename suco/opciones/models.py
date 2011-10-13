# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *

# Create your models here.

class ManejoAgro(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso opciones de manejo agroecologico"
    
CHOICE_NIVEL_CONOCIMIENTO = ((1,'Nada'),(2,'Poco'),(3,'Algo'),(4,'Bastante'))

class OpcionesManejo(models.Model):
    ''' opciones de manejo agroecologico
    '''
    uso = models.ForeignKey(ManejoAgro, verbose_name="Uso de opciones de manejo agroecologico")
    nivel = models.IntegerField('Nivel de conocimiento', choices=CHOICE_NIVEL_CONOCIMIENTO)
    menor_escala = models.IntegerField('Han experimentado en pequeña escala', choices=CHOICE_OPCION)
    mayor_escala = models.IntegerField('Han experimentado en mayor escala', choices=CHOICE_OPCION)
    volumen = models.FloatField('¿Qué área, número o volumen')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.uso.nombre
    
    class Meta:
        verbose_name_plural = "Opciones de manejo"
        
class Observacion(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class Sistematica(models.Model):
    tipo = models.ManyToManyField(Observacion, verbose_name="Observaciones", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Observación sistemática de"

# Uso de semilla
        
class CultivosVariedad(models.Model):
    cultivo = models.CharField(max_length=200)
    def __unicode__(self):
        return self.cultivo

    class Meta:
        verbose_name_plural = "Cultivos variedad"
        ordering = ['cultivo']

class Variedades(models.Model):
    cultivo = models.ForeignKey(CultivosVariedad)
    variedad = models.CharField(max_length=200)
    def __unicode__(self):
        return '%s - %s' % (self.cultivo.cultivo, self.variedad)

    class Meta:
        verbose_name_plural = "Variedades"
        ordering = ['cultivo']
        
CHOICE_ORIGEN = ((1,'Nativo'), (2,'Introducido'))

class Semilla(models.Model):
    ''' uso de semilla
    '''
    cultivo = models.ForeignKey(Variedades, verbose_name="cultivo y su variedad",
                                help_text="Escoja el cultivo con su variedad")
    origen = models.IntegerField('Origen', choices=CHOICE_ORIGEN)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivo.cultivo
    
    class Meta:
        verbose_name_plural = "Uso de Semilla"
        
# participación de la familia en: labores, beneficios y la toma de decisiones

class Rubros(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class Decision(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class Participasion(models.Model):
    rubro = models.ForeignKey(Rubros)
    labores = models.ManyToManyField(Decision, verbose_name="Labores", related_name="labore")
    beneficios = models.ManyToManyField(Decision, verbose_name="Beneficios", related_name="beneficio")
    decision = models.ManyToManyField(Decision, verbose_name="Decisión", related_name="decision")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Participación de la familia en: labores, beneficios y la toma de decisión"
        
# Suelo

class Textura(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Textura"

class Profundidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Profundidad"

# Esta clase de va a ocupar en varias de los tipos de caraterización
# ya que contendra las opciones Alta, Media y Baja
class Densidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Densidad"

class Pendiente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Pendiente"

class Drenaje(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Drenaje"
        
class Suelo(models.Model):
    ''' Caracterización de terreno
    '''
    textura = models.ManyToManyField(Textura,
                                     verbose_name="¿Cúal es el tipo de textura del suelo?")
    profundidad = models.ManyToManyField(Profundidad,
                                         verbose_name="¿Cúal es la profundidad del suelo?")
    lombrices = models.ManyToManyField(Densidad,
                                       verbose_name="¿Cómo es la presencia de lombrice en el suelo?",
                                       related_name="lombrices")
    densidad = models.ManyToManyField(Densidad,
                                      verbose_name="¿Cómo es la densidad de raiz en la capa productiva de suelo?",
                                      related_name="densidad")
    pendiente = models.ManyToManyField(Pendiente,
                                       verbose_name="¿Cúal es la pendiente del terrreno?")
    drenaje = models.ManyToManyField(Drenaje,
                                     verbose_name="¿Cómo es el drenaje del suelo?")
    materia = models.ManyToManyField(Densidad,
                                     verbose_name="Cómo en el contenido de materia orgánica",
                                     related_name="materia")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Suelo"
        
#Manejo del suelo
        
class Preparar(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - preparar"
       
class Traccion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - tracción"

class Fertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - fertilizacion"

class Conservacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - conservacion"

class ManejoSuelo(models.Model):
    ''' 12.2 Manejo de suelo
    '''
    preparan = models.ManyToManyField(Preparar, verbose_name="¿Cómo preparan sus terrenos?")
    traccion = models.ManyToManyField(Traccion,
                                      verbose_name="¿Qué tipo de traccion utiliza para la preparación del suelo?")
    analisis = models.IntegerField('¿Realiza análisis de fertilidad del suelo', choices=CHOICE_OPCION)
    fertilizacion = models.ManyToManyField(Fertilizacion, verbose_name="¿Qué tipo de fertilización realiza")
    practica = models.IntegerField('¿Realiza práctica de conservación de suelo', choices=CHOICE_OPCION)
    obra = models.ManyToManyField(Conservacion, verbose_name="¿Qué tipo de obra de conservación de suelo?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Manejo de Suelo"
        
class Procesado(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
CHOICE_EMPAQUE = (  (1,'Biodegradable'),
                    (2,'Contaminante'),
                    (3,'Reutilisable')
                 )
                 
class Procesamiento(models.Model):
    producto = models.ForeignKey(Procesado, verbose_name="Producto Procesado")
    cantidad = models.FloatField()
    aditivos = models.IntegerField('Uso de aditivos', choices=CHOICE_OPCION)
    empaque = models.IntegerField('Tipo de empaque', choices=CHOICE_EMPAQUE)
    comercializada = models.FloatField('Cantidad comercializada')
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Procesamiento de la producción"
    
# Otros ingresos de toda la familiar

class Fuente(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
        
class TipoTrabajo(models.Model):
    fuente = models.ForeignKey(Fuente)
    nombre =  models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s - %s' % (self.fuente.nombre, self.nombre)

CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))
        
class OtrosIngresos(models.Model):
    trabajo = models.ForeignKey(TipoTrabajo, verbose_name="Tipo de trabajo")
    meses = models.IntegerField('# Meses')
    Ingreso = models.FloatField('Ingreso por mes')
    total = models.FloatField('Ingreso total por año')
    tiene_ingreso = models.IntegerField('¿Quienes tienen ingresos?', choices=CHOICE_MANEJA)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Otros Ingresos de toda la familia"
    
    
