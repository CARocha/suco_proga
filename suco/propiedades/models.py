# -*- coding: UTF-8 -*-

from django.db import models
from suco.encuesta.models import *
from suco.organizaciones.models import *

# Create your models here.

CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"))
CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),
                    (4,"Minifalda"),(5,"Ladrillo o Bloque"),(6,"Taquezal"))

class Piso(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Pisos"

class Techo(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Techos"

class TipoCasa(models.Model):
    '''Modelo tipos de casa
    '''
    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
    piso = models.ManyToManyField(Piso, verbose_name="Piso de la casa")
    techo = models.ManyToManyField(Techo, verbose_name="Techo de la casa")
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_tipo_display()

    class Meta:
        verbose_name_plural = "Tipos de Casas"

class DetalleCasa(models.Model):
    '''Modelo detalle de casa
    '''
    tamano = models.IntegerField('Tamaño en mt cuadrado',null=True, blank=True)
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE,null=True, blank=True)
    letrina = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    lavadero = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % str(self.tamano)

    class Meta:
        verbose_name_plural = "Detalle casa"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Equipos"


class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Infraestructuras"
        
class Electro(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Electrodomésticos"
        
class Sanamiento(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Equipos para seneamiento ambiental"

class PropiedadEquipo(models.Model):
    '''Modelo propiedades
    '''
    equipo = models.ForeignKey(Equipos)
    cantidad = models.IntegerField('Cantidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.equipo.nombre
    
    class Meta:
        verbose_name_plural = "Equipos para la producción"
     
class PropiedadInfra(models.Model):  
    infraestructura = models.ForeignKey(Infraestructuras, verbose_name="Infraestructuras")
    cantidad = models.IntegerField('Cantidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.infraestructura.nombre
    
    class Meta:
        verbose_name_plural = "Infraestructura para la produccion"
    
class Electrodomestico(models.Model):  
    electro = models.ForeignKey(Electro, verbose_name="Electrodomésticos")
    cantidad = models.IntegerField('Cantidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.electro.nombre
    
    class Meta:
        verbose_name_plural = "Electrodomésticos"
    
class Sana(models.Model):  
    electro = models.ForeignKey(Sanamiento, verbose_name="Equipos para saneamiento ambiental")
    cantidad = models.IntegerField('Cantidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.electro.nombre
    
    class Meta:
        verbose_name_plural = "Equipos para seneamiento ambiental"
        
#Herramientas

class NombreHerramienta(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Herramientas-Nombres"


class Herramientas(models.Model):
    '''Modelo herramientas
    '''
    herramienta = models.ForeignKey(NombreHerramienta)
    numero = models.IntegerField('Número')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.herramienta.nombre

    class Meta:
        verbose_name_plural = "Herramientas"


class NombreTransporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Transporte-Nombre"


class Transporte(models.Model):
    '''Modelo transporte
    '''
    transporte = models.ForeignKey(NombreTransporte)
    numero = models.IntegerField('Número')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.transporte.nombre
    
    class Meta:
        verbose_name_plural = "Transporte"

#Ahorro

CHOICE_AHORRO = (   (1,"Si"),
                    (2,"No"),
                    (3,"Menos de 5 años"),
                    (4,"Mas de 5 años")
                 )
                 
class AhorroPregunta(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Ahorro-Preguntas"   
    def __unicode__(self):
        return self.nombre
    
class Ahorro(models.Model):
    ''' modelos ahorro
    '''
    ahorro = models.ForeignKey(AhorroPregunta)
    respuesta = models.IntegerField(choices=CHOICE_AHORRO)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return self.ahorro.nombre
    
    class Meta:
        verbose_name_plural = "Ahorro de la o el joven participante"
        
# credito

class DaCredito(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Credito-Dacredito"


class OcupaCredito(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Credito-Ocupa"


CHOICE_SATISFACCION = ( (1,"Menos de 25 % de las necesidades"),
                        (2,"Entre 25 y 50 % de las necesidades"),
                        (3,"Entre 50 y 100 % de las necesidades")
                      )

class Credito(models.Model):
    ''' Modelo de credito
    '''
    recibe = models.IntegerField('Recibe Crédito', choices= CHOICE_OPCION,
                                 null=True, blank=True)
    desde = models.IntegerField('Desde cuando', choices= CHOICE_DESDE,
                                 null=True, blank=True)
    quien_credito = models.ManyToManyField(DaCredito, verbose_name="De quien recibe credito",
                                           null=True, blank=True)
    ocupa_credito = models.ManyToManyField(OcupaCredito, verbose_name="Para que ocupa el credito",
                                           null=True, blank=True)
    satisfaccion = models.IntegerField('Satisfacción de la demanda de crédito',
                                       choices= CHOICE_SATISFACCION, blank=True, null=True)
    dia = models.IntegerField('Esta al dia con su Crédito', choices=CHOICE_OPCION,
                              null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_recibe_display()
    
    class Meta:
        verbose_name_plural = "Credito en efectivo y/o materiales de la o el joven participante"
