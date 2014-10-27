from django.db import models
from suco.lugar.models import *

# Create your models here.

CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no
CHOICE_SEXO = ( (1,'Hombre'),
                (2,'Mujer')
              )
CHOICE_ACTIVO = (
    (0, "No activo"),
    (1, "Activo en SUCO")
)

class Grupo(models.Model):
    nombre = models.CharField('Nombre del grupo', max_length=200)
    def __unicode__(self):
        return self.nombre

class Joven(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    cedula = models.CharField('Cedula', max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    grupo = models.ForeignKey(Grupo)
    idseguimiento = models.IntegerField()
    centroregional = models.ForeignKey(Centroregional)
    activo = models.IntegerField(choices=CHOICE_ACTIVO, verbose_name=u'Activo?', default=1)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Jovenes"
        ordering = ('nombre',)