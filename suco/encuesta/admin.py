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
from django.contrib.auth.models import User

class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    max_num = None
    can_delete = False
    
class ProduccionConsumoInline(admin.TabularInline):
    model = ProduccionConsumo
    extra = 1
    max_num = None
    can_delete = False

class CultivoPastoInline(admin.TabularInline):
    model = CultivoPasto
    extra = 1
    max_num = 5
    can_delete = False
    
class divisionInline(admin.TabularInline):
    model = division
    extra = 1
    max_num = 1
    can_delete = False
    
class CultivosInline(admin.TabularInline):
    model = Cultivos
    extra = 1
    max_num = None
    #can_delete = False
    
class CultivosPatioInline(admin.TabularInline):
    model = CultivosPatio
    extra = 1
    max_num = None
    #can_delete = False
    
class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 2
    can_delete = False
    
class SaludInline(admin.TabularInline):
    model = Salud
    extra = 1
    max_num = 2
    can_delete = False
    
class EnergiaInline(admin.TabularInline):
    model = Energia
    extra = 1
    max_num = 5
    can_delete = False
    
class QueUtilizaInline(admin.TabularInline):
    model = QueUtiliza
    extra = 1
    max_num = 1
    can_delete = False
    
class AguaConsumoInline(admin.TabularInline):
    model = AguaConsumo
    extra = 1
    max_num = 1
    can_delete = False
    
class AguaProduccionInline(admin.TabularInline):
    model = AguaProduccion
    extra = 1
    max_num = 1
    can_delete = False
    
class AccesoTierraInline(admin.TabularInline):
    model = AccesoTierra
    extra = 1
    max_num = 1
    can_delete = False
#    radio_fields = {"tierra": admin.VERTICAL,
#                    "parcela": admin.VERTICAL,
#                    "casa": admin.VERTICAL,
#                    "documento": admin.HORIZONTAL}
    
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = None
    can_delete = False
    
class AccesoAguaInline(admin.TabularInline):
    model = AccesoAgua
    extra = 1
    max_num = 1
    can_delete = False
    
class ExistenciaArbolesInline(admin.TabularInline):
    model = ExistenciaArboles
    fields = ['maderable', 'cantidad_maderable', 'forrajero', 'cantidad_forrajero',
              'energetico', 'cantidad_energetico', 'frutal', 'cantidad_frutal']
    extra = 1
    max_num = 1
    can_delete = False
    
class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    max_num = 10
    can_delete = False
    
class OpcionesManejoInline(admin.TabularInline):
    model = OpcionesManejo
    extra = 1
    max_num = None
    can_delete = False
    
class SistematicaInline(admin.TabularInline):
    model = Sistematica
    extra = 1
    max_num = 1
    can_delete = False
    
class SemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    max_num = None
    can_delete = False

class ParticipasionInline(admin.TabularInline):
    model = Participasion
    extra = 1
    max_num = 7
    can_delete = False
    
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 1
    can_delete = False
    
class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    fields = ['preparan', 'traccion', 'analisis','fertilizacion','practica','obra']
    extra = 1
    max_num = 1
    can_delete = False
    
class ProcesamientoInline(admin.TabularInline):
    model = Procesamiento
    extra = 1
    max_num = None
    can_delete = False
    
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    max_num = None
    can_delete = False
    
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    fields = ['socio', 'desde_socio']
    extra = 1
    max_num = 1
    can_delete = False
    
class OrganizacionComunitariaInline(admin.TabularInline):
    model = OrganizacionComunitaria
    extra = 1
    max_num = 1
    can_delete = False
    
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class PropiedadEquipoInline(admin.TabularInline):
    model = PropiedadEquipo
    extra = 1
    max_num = None
    can_delete = False
    
class PropiedadInfraInline(admin.TabularInline):
    model = PropiedadInfra
    extra = 1
    max_num = None
    can_delete = False
    
class ElectrodomesticoInline(admin.TabularInline):
    model = Electrodomestico
    extra = 1
    max_num = None
    can_delete = False
    
class SanaInline(admin.TabularInline):
    model = Sana
    extra = 1
    max_num = None
    can_delete = False
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    max_num = None
    can_delete = False
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    max_num = None
    can_delete = False
    
class AhorroInline(admin.TabularInline):
    model = Ahorro
    extra = 1
    max_num = None
    can_delete = False
    
class CreditoInline(admin.TabularInline):
    model = Credito
    fields = ['recibe', 'desde','quien_credito','ocupa_credito','satisfaccion','dia']
    extra = 1
    max_num = 1
    can_delete = False
    
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    max_num = None
    can_delete = False
    
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    max_num = 13
    can_delete = False
    
class RiesgosInline(admin.TabularInline):
    model = Riesgos
    extra = 1
    max_num = 6
    can_delete = False
        
class EncuestaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        #if getattr(obj, 'usuario', None) is None:
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(EncuestaAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
        
    save_on_top = True
    actions_on_top = True
    exclude = ('usuario',)
    inlines = [EducacionInline,SaludInline,EnergiaInline,QueUtilizaInline,AguaConsumoInline,
               AguaProduccionInline,OrganizacionGremialInline,OrganizacionComunitariaInline,
               AccesoTierraInline,UsoTierraInline,AccesoAguaInline,ExistenciaArbolesInline,
               ReforestacionInline,AnimalesFincaInline,ProduccionConsumoInline,CultivoPastoInline,divisionInline,
               CultivosInline,CultivosPatioInline,OpcionesManejoInline,SistematicaInline,SemillaInline,
               ParticipasionInline,SueloInline,ManejoSueloInline,ProcesamientoInline,
               TipoCasaInline,DetalleCasaInline,PropiedadEquipoInline,PropiedadInfraInline,
               ElectrodomesticoInline,SanaInline,HerramientasInline,TransporteInline,OtrosIngresosInline,
               AhorroInline, CreditoInline,SeguridadInline,VulnerableInline,RiesgosInline
              ]
    list_display = ('nombre', 'formacion', 'comunidad', 'escolaridad')
    list_filter = ['comunidad', 'formacion']
    search_fields = ['nombre', 'comunidad__nombre', 'formacion__nombre']
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
admin.site.register(Traccion)
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
admin.site.register(ManejoAgro)
admin.site.register(TipoTrabajo)
admin.site.register(AquienVende)
admin.site.register(Patio)
