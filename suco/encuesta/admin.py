# -*- coding: UTF-8 -*-

from django.contrib import admin
from suco.animal_produccion.models import *
from suco.cultivos.models import *
from suco.encuesta.models import *
from suco.familias.models import *
from suco.finca_tierra.models import *
from suco.lugar.models import *
from suco.opciones.models import *
from suco.organizaciones.models import *
from suco.propiedades.models import *
from suco.seguridad.models import *

class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    max_num = 1
    
class ProduccionConsumoInline(admin.TabularInline):
    model = ProduccionConsumo
    extra = 1
    max_num = 1

class CultivoPastoInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    max_num = 1
    
class CultivosInline(admin.TabularInline):
    model = Cultivos
    extra = 1
    max_num = 1
    
class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 1
    
class SaludInline(admin.TabularInline):
    model = Salud
    extra = 1
    max_num = 1
    
class EnergiaInline(admin.TabularInline):
    model = Energia
    extra = 1
    max_num = 1
    
class QueUtilizaInline(admin.TabularInline):
    model = QueUtiliza
    extra = 1
    max_num = 1
    
class AguaConsumoInline(admin.TabularInline):
    model = AguaConsumo
    extra = 1
    max_num = 1
    
 class AguaProduccionInline(admin.TabularInline):
    model = AguaProduccion
    extra = 1
    max_num = 1
    
class AccesoTierraInline(admin.TabularInline):
    model = AccesoTierra
    extra = 1
    max_num = 1
    
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 1
    
class AccesoAguaInline(admin.TabularInline):
    model = AccesoAgua
    extra = 1
    max_num = 1
    
class ExistenciaArbolesInline(admin.TabularInline):
    model = ExistenciaArboles
    extra = 1
    max_num = 1
    
class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    max_num = 1
    
class OpcionesManejoInline(admin.TabularInline):
    model = OpcionesManejo
    extra = 1
    max_num = 1
    
class SistematicoInline(admin.TabularInline):
    model = Sistematica
    extra = 1
    max_num = 1
    
class SemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    max_num = 1

class ParticipasionInline(admin.TabularInline):
    model = Participasion
    extra = 1
    max_num = 1
    
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 1
    
class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    extra = 1
    max_num = 1
    
class ProcesamientoInline(admin.TabularInline):
    model = Procesamiento
    extra = 1
    max_num = 1
    
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    max_num = 1
    
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    extra = 1
    max_num = 1
    
class OrganizacionComunitariaInline(admin.TabularInline):
    model = OrganizacionComunitaria
    extra = 1
    max_num = 1
    
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    
class PropiedadEquipoInline(admin.TabularInline):
    model = PropiedadEquipo
    extra = 1
    max_num = 1
    
class PropiedadInfraInline(admin.TabularInline):
    model = PropiedadInfra
    extra = 1
    max_num = 1
    
class ElectrodomesticoInline(admin.TabularInline):
    model = Electrodomestico
    extra = 1
    max_num = 1
    
class SanaInline(admin.TabularInline):
    model = Sana
    extra = 1
    max_num = 1
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    max_num = 1
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    max_num = 1
    
class AhorroInline(admin.TabularInline):
    model = Ahorro
    extra = 1
    max_num = 1
    
class CreditoInline(admin.TabularInline):
    model = Credito
    extra = 1
    max_num = 1
    
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    max_num = 1
    
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    max_num = 1
    
class RiesgosInline(admin.TabularInline):
    model = Riesgos
    extra = 1
    max_num = 1
    
   
   
class EncuestaAdmin(admin.ModelAdmin):
#    def queryset(self, request):
#        if request.user.is_superuser:
#            return Encuesta.objects.all()
#        return Encuesta.objects.filter(user=request.user)

#    def get_form(self, request, obj=None, ** kwargs):
#        if request.user.is_superuser:
#            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
#        else:
#            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
#            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
#        return form
        
    save_on_top = True
    actions_on_top = True
    inlines = [AnimalesFincaInline,ProduccionConsumoInline,CultivoPastoInline,
               CultivosInline,EducacionInline,SaludInline,EnergiaInline,
              ]
    list_display = ('nombre', 'finca', 'comunidad', 'organizacion')
    list_filter = ['comunidad', 'organizacion']
    search_fields = ['nombre', 'comunidad__nombre', 'organizacion__nombre']
    date_hierarchy = 'fecha'
               
admin.site.register(Encuesta, EncuestaAdmin)

#utility :P
admin.site.register(Animales)
admin.site.register(ProductoAnimal)
admin.site.register(Pastos)
admin.site.register(Componente)
admin.site.register(TipoCultivos)
admin.site.register(PreguntaEnergia)
admin.site.register(Cocinar)
admin.site.register(FuenteConsumo)
admin.site.register(TrataAgua)
admin.site.register(DisponibilidadAgua)
admin.site.register(FuenteProduccion)
admin.site.register(EquipoBombeo)
admin.site.register(EnergiaUtiliza)
admin.site.register(Acceso)
admin.site.register(Parcela)
admin.site.register(Solar)
admin.site.register(Documento)
admin.site.register(Uso)
admin.site.register(AguaAcceso)
admin.site.register(Maderable)
admin.site.register(Forrajero)
admin.site.register(Energetico)
admin.site.register(Frutal)
admin.site.register(Actividad)
admin.site.register(Observacion)
admin.site.register(CultivosVariedad)
admin.site.register(Variedades)
admin.site.register(Rubros)
admin.site.register(Decision)
admin.site.register(Textura)
admin.site.register(Profundidad)
admin.site.register(Densidad)
admin.site.register(Pendiente)
admin.site.register(Drenaje)
admin.site.register(Preparar)
admin.site.register(traccion)
admin.site.register(Fertilizacion)
admin.site.register(Conservacion)
admin.site.register(Procesado)
admin.site.register(Fuente)
admin.site.register(OrgGremiales)
admin.site.register(OrgComunitarias)
admin.site.register(BeneficioOrgComunitaria)
admin.site.register(NoOrganizado)
admin.site.register(Piso)
admin.site.register(Techo)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(Electro)
admin.site.register(Sanamiento)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)
admin.site.register(AhorroPregunta)
admin.site.register(DaCredito)
admin.site.register(OcupaCredito)
admin.site.register(Componentes)
admin.site.register(Alimentos)
admin.site.register(Causa)
admin.site.register(Fenomeno)
admin.site.register(Graves)
admin.site.register(PreguntaRiesgo)
admin.site.register(Recolector)
admin.site.register(Escolaridad)
admin.site.register(Tecnica)
admin.site.register(ParticipacionProyecto)
