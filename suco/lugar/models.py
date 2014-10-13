from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=80, unique= True)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"

class Centroregional(models.Model):
    nombre = models.CharField('Nombre del Centro', max_length=200)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Centros regionales"

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")
    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null = True)
    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null = True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Municipios"

class Comunidad(models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=40)

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural="Comunidad"

    def __unicode__(self):
        return self.nombre        
