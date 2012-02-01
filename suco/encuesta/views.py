# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist
from decorators import session_required
from datetime import date
from forms import *
from decimal import Decimal

from suco.encuesta.models import *
from suco.animal_produccion.models import *
from suco.cultivos.models import *
from suco.familias.models import *
from suco.finca_tierra.models import *
from suco.lugar.models import *
from suco.opciones.models import *
from suco.organizaciones.models import *
from suco.propiedades.models import *
from suco.seguridad.models import *

from utils import grafos
from utils import *

# Create your views here.

def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))
        
#-------------------------------------------------------------------------------
        
def _queryset_filtrado(request):
    '''metodo para obtener el queryset de encuesta 
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    anio = int(request.session['fecha'])
    #diccionario de parametros del queryset
    params = {}
    if 'fecha' in request.session:
        params['fecha__year'] = anio

        if 'departamento' in request.session:
            #incluye municipio y comunidad
            if request.session['municipio']:                
                if 'comunidad' in request.session and request.session['comunidad'] != None:
                    params['comunidad'] = request.session['comunidad']                    
                else:
                    params['comunidad__municipio'] = request.session['municipio']                                        
            else:
                params['comunidad__municipio__departamento'] = request.session['departamento']

        if 'sexo' in  request.session:
            params['sexo'] = request.session['sexo']
            
#        if 'organizacion' in request.session:
#            params['beneficiario'] = request.session['organizacion']            

        if 'duenio' in  request.session:
            params['accesotierra__documento'] = request.session['duenio']
        
        unvalid_keys = []
        for key in params:
            if not params[key]:
                unvalid_keys.append(key)
        
        for key in unvalid_keys:
            del params[key]
        
        return Encuesta.objects.filter(**params)

#-------------------------------------------------------------------------------

# Comienza la parte del index
'''
def inicio(request):

    if request.method == 'POST':
        mensaje = None
        form = MonitoreoForm(request.POST)
        if form.is_valid():            
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            try:
                municipio = Municipio.objects.get(id=int(form.cleaned_data['municipio'])) 
            except:
                municipio = None
            try:
                comunidad = Comunidad.objects.get(id=int(form.cleaned_data['comunidad']))                
            except:
                comunidad = None

            request.session['municipio'] = municipio 
            request.session['comunidad'] = comunidad
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['duenio'] = form.cleaned_data['dueno']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
        print 'hola'
        return HttpResponseRedirect('/menu')           
    else:
        form = MonitoreoForm()
        mensaje = "Existen alguno errores"
    
    shva = request.GET.get('shva', '')
    if shva and request.session['activo']:
        shva = 1
    
    dict = {'form': form,'user': request.user, 'shva':shva}
    return render_to_response('encuestas/inicio.html', dict,
                              context_instance=RequestContext(request))        
'''
def menu(request):
    return render_to_response('encuestas/menu.html',
                              context_instance=RequestContext(request)) 

#-------------------------------------------------------------------------------
def index(request):
    if request.method == 'POST':
        mensaje = None
        form = MonitoreoForm(request.POST)
        if form.is_valid():            
#            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            try:
                municipio = Municipio.objects.get(id=int(form.cleaned_data['municipio'])) 
            except:
                municipio = None
            try:
                comunidad = Comunidad.objects.get(id=int(form.cleaned_data['comunidad']))                
            except:
                comunidad = None

            request.session['municipio'] = municipio 
            request.session['comunidad'] = comunidad
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['duenio'] = form.cleaned_data['dueno']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            return HttpResponseRedirect('/menu') 
    else:
        form = MonitoreoForm()
        mensaje = "Existen alguno errores"
    dict = {'form': form,'user': request.user, }
    
    depart = []
    var=0
    for depar in Departamento.objects.all():
        conteo = Encuesta.objects.filter(comunidad__municipio__departamento=depar).aggregate(conteo=Count('comunidad__municipio__departamento'))['conteo']
        if conteo != 0:
            var += 1
            depart.append([depar.nombre,conteo,var])
    mujeres = Encuesta.objects.filter(sexo=2).count()
    hombres = Encuesta.objects.filter(sexo=1).count()  
    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))      
        
#-------------------------------------------------------------------------------
def generales(request):
    numero = Encuesta.objects.all().count()
    
    mujeres = Encuesta.objects.filter(sexo=2).count()
    por_mujeres = round(saca_porcentajes(mujeres,numero),2)
    hombres = Encuesta.objects.filter(sexo=1).count()
    por_hombres = round(saca_porcentajes(hombres,numero),2)  
    
    #Educacion
    escolaridad = []
    for escuela in CHOICE_EDUCACION:
        conteo = Encuesta.objects.filter(educacion__sexo=escuela[0]).aggregate(conteo=Count('educacion__sexo'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,numero),2)
        escolaridad.append([escuela[1],conteo,porcentaje])
        
        
    #Departamentos   
    depart = []
    valores_d = []
    leyenda_d = []  
    for depar in Departamento.objects.all():
        conteo = Encuesta.objects.filter(comunidad__municipio__departamento=depar).aggregate(conteo=Count('comunidad__municipio__departamento'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,numero))
        if conteo != 0:
            depart.append([depar.nombre,conteo,porcentaje])
            valores_d.append(conteo)
            leyenda_d.append(depar.nombre)
            
    grafo_depart = grafos.make_graph(valores_d, leyenda_d, 'Departamentos Encuestados', return_json=False ,type=grafos.PIE_CHART_2D)

    #Municipios        
    munis = []
    valores_m = []
    leyenda_m = []
    for mun in Municipio.objects.all():
        conteo = Encuesta.objects.filter(comunidad__municipio=mun).aggregate(conteo=Count('comunidad__municipio'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,numero))
        if conteo != 0:
            munis.append([mun.nombre,conteo,porcentaje])
            valores_m.append(conteo)
            leyenda_m.append(mun.nombre)
      
    grafo_munis = grafos.make_graph(valores_m, leyenda_m, 'Municipios Encuestados', return_json=False ,type=grafos.PIE_CHART_2D)
            

    return render_to_response('encuestas/generales.html', locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla Educación
@session_required
def educacion(request):
    '''Tabla de educacion 
    '''
    #*******Variables globales**********
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #**********************************
    
    tabla_educacion = []
    grafo = []
    suma = 0 
    for e in CHOICE_EDUCACION:
        objeto = a.filter(educacion__sexo = e[0]).aggregate(num_total = Sum('educacion__total'),
                no_leer = Sum('educacion__no_leer'), 
                p_incompleta = Sum('educacion__p_incompleta'), 
                p_completa = Sum('educacion__p_completa'), 
                s_incompleta = Sum('educacion__s_incompleta'),
                bachiller = Sum('educacion__bachiller'), 
                universitario = Sum('educacion__universitario'),
                f_comunidad = Sum('educacion__f_comunidad'))
        try:
            suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
        except:
            pass
        variable = round(saca_porcentajes(suma,objeto['num_total']))
        grafo.append([e[1],variable])
        
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                saca_porcentajes(objeto['f_comunidad'], objeto['num_total'], False)]
        tabla_educacion.append(fila)
    
    return render_to_response('familias/educacion.html', locals(),
                                  context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla Salud       
@session_required
def salud(request):
    '''salud'''
    #*******Variables globales**********
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #**********************************
    
    numero = a.count()
    tabla_estado = []
    tabla_sitio = []

    for choice in CHOICE_EDUCACION:
        query = a.filter(salud__sexo=choice[0])
        casos = query.count()
        resultados = query.aggregate(bs = Sum('salud__b_salud'),
                                     ds = Sum('salud__s_delicada'),
                                     ec = Sum('salud__e_cronica'),
                                     centro = Sum('salud__v_centro'),
                                     medico = Sum('salud__v_medico'),
                                     naturista = Sum('salud__v_naturista'),
                                     automedica = Sum('salud__automedica')
                                     )
        
        #validando que no sea none
        if resultados['bs']:
            total_estado = resultados['bs'] 
        else:
            total_estado = 0

        if resultados['ds']:
            total_estado += resultados['ds'] 
        
        if resultados['ec']:
            total_estado += resultados['ec']

        fila_estado = [choice[1], casos,
                saca_porcentajes(resultados['bs'], total_estado, False),
                saca_porcentajes(resultados['ds'], total_estado, False),
                saca_porcentajes(resultados['ec'], total_estado, False)]
        tabla_estado.append(fila_estado)

        total_sitio = 0
        if resultados['centro']:
            total_sitio += resultados['centro']
        if resultados['medico']:
            total_sitio += resultados['medico']
        if resultados['naturista']:
            total_sitio += resultados['naturista']
        if resultados['automedica']:
            total_sitio += resultados['automedica']

        fila_sitio = [choice[1], casos,
                      saca_porcentajes(resultados['centro'], total_sitio, False),
                      saca_porcentajes(resultados['medico'], total_sitio, False),
                      saca_porcentajes(resultados['naturista'], total_sitio, False),
                      saca_porcentajes(resultados['automedica'], total_sitio, False),
                    ]
        tabla_sitio.append(fila_sitio)

    return render_to_response('familias/salud.html', 
                              locals(),
                              context_instance=RequestContext(request))  
#Tabla Energia
@session_required
def luz(request):
    '''Tabla de acceso a energia electrica'''
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    tabla = []
    total_tiene_luz = 0            

    for choice in PreguntaEnergia.objects.all():
        query = consulta.filter(energia__pregunta=choice, energia__respuesta=1).distinct()
        resultados = query.count() 
        if choice.pregunta == 1:
            total_tiene_luz = resultados 
            fila = [choice.pregunta, 
                    resultados,
                    saca_porcentajes(resultados, consulta.count(), False)]
            tabla.append(fila)
        else:
            fila = [choice.pregunta, 
                    resultados,
                    saca_porcentajes(resultados, consulta.count(), False)]
            tabla.append(fila)
    tabla_cocina = []        
    for cocina in Cocinar.objects.all():
        conteo = consulta.filter(queutiliza__cocina=cocina).count()
        porcentaje = round(saca_porcentajes(conteo,consulta.count()))
        tabla_cocina.append([cocina.nombre,conteo,porcentaje])

    return render_to_response('familias/luz.html', 
                              locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla Agua
@session_required
def agua(request):
    '''Agua'''
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    tabla = []
    total = consulta.aggregate(total=Count('aguaconsumo__fuente'))
    #Esta parte es la agua para consumo: Fuentes
    for choice in FuenteConsumo.objects.all():
        query = consulta.filter(aguaconsumo__fuente=choice)
        numero = query.count()
        fila = [choice.nombre, numero,
                saca_porcentajes(numero, consulta.count(), False)
                ]
        tabla.append(fila)

    totales = [consulta.count(), 100]
    #agua para consumo: Tratan
    tratar = []
    for trata in TrataAgua.objects.all():
        query = consulta.filter(aguaconsumo__tratar=trata).count()
        fila = [trata.nombre,query,
                saca_porcentajes(query,consulta.count(), False)
               ]
        tratar.append(fila)
        
    disponibilidad = []
    for trata in DisponibilidadAgua.objects.all():
        query = consulta.filter(aguaconsumo__disponible=trata).count()
        fila = [trata.nombre,query,
                saca_porcentajes(query,consulta.count(), False)
               ]
        disponibilidad.append(fila)
        
    fuentes = []
    for trata in FuenteProduccion.objects.all():
        query = consulta.filter(aguaproduccion__fuente=trata).count()
        fila = [trata.nombre,query,
                saca_porcentajes(query,consulta.count(), False)
               ]
        fuentes.append(fila)

    bombeo = []
    for trata in EquipoBombeo.objects.all():
        query = consulta.filter(aguaproduccion__equipo=trata).count()
        fila = [trata.nombre,query,
                saca_porcentajes(query,consulta.count(), False)
               ]
        bombeo.append(fila)
        
    energia = []
    for trata in EnergiaUtiliza.objects.all():
        query = consulta.filter(aguaproduccion__energia=trata).count()
        fila = [trata.nombre,query,
                saca_porcentajes(query,consulta.count(), False)
               ]
        energia.append(fila)              
    return render_to_response('familias/agua.html', 
                              locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#GRAFICOS
@session_required
def organizacion_grafos(request, tipo):
    '''grafos de organizacion
       tipo puede ser: beneficio, miembro'''
    consulta = _queryset_filtrado(request)
    
    data = [] 
    legends = []
    if tipo == 'beneficio':
        for opcion in BeneficiosObtenido.objects.all():
            data.append(consulta.filter(organizaciongremial__beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'miembro':
        for opcion in SerMiembro.objects.all():
            data.append(consulta.filter(organizaciongremial__beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                'Porque soy o quiero ser miembro de la junta directiva o las comisiones', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'estructura':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(organizaciongremial__asumir_cargo=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                'Si no es miembro de ninguna estructura ¿estaria interesado en asumir cargos?', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'beneficiorganizado':
        for opcion in BeneficioOrgComunitaria.objects.all():
            data.append(consulta.filter(organizacioncomunitaria__cual_beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿Cuáles son los beneficios de estar organizado', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'norganizado':
        for opcion in NoOrganizado.objects.all():
            data.append(consulta.filter(organizacioncomunitaria__no_organizado=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿Porqué no esta organizado?', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'comunitario':
        for opcion in OrgComunitarias.objects.all():
            comu = consulta.filter(organizacioncomunitaria__cual_organizacion=opcion).count()
            if comu > 0:
                data.append(comu)
                legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿A cual organizacion comunitaria pertenece', return_json = True,
                type = grafos.PIE_CHART_2D)
    else:
        raise Http404
            
@session_required
def agua_grafos_disponibilidad(request, tipo):
    '''Tipo: numero del 1 al 6 en CHOICE_FUENTE_AGUA'''
    consulta = _queryset_filtrado(request)
    data = [] 
    legends = []
    tipo = get_object_or_404(Fuente, id = int(tipo)) 
    for opcion in Disponibilidad.objects.all():
        data.append(consulta.filter(agua__disponible=opcion, agua__fuente = tipo).count())
        legends.append(opcion.nombre)
    titulo = 'Disponibilidad del agua en %s' % tipo.nombre 
    return grafos.make_graph(data, legends, 
            titulo, return_json = True,
            type = grafos.PIE_CHART_2D)
            
@session_required
def fincas_grafos(request, tipo):
    '''Tipo puede ser: tenencia, solares, propietario'''
    consulta = _queryset_filtrado(request)
    #CHOICE_TENENCIA, CHOICE_DUENO
    data = [] 
    legends = []
    if tipo == 'tenencia':
        for opcion in Acceso.objects.all():
            data.append(consulta.filter(accesotierra__tierra=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿De quien es la tierra que usted va a trabajar?', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'casa':
        for opcion in Solar.objects.all():
            data.append(consulta.filter(accesotierra__casa=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                '¿De quien es la casa donde vive?', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'propietario':
        for opcion in Parcela.objects.all():
            data.append(consulta.filter(accesotierra__parcela=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                'Dueño de propiedad', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'documento':
        for opcion in Documento.objects.all():
            data.append(consulta.filter(accesotierra__documento=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                'Documento legal de la propiedad, a nombre a quién', return_json = True,
                type = grafos.PIE_CHART_2D)
    else:
        raise Http404 
        
@session_required
def grafo_manejosuelo(request, tipo):
    #--- variables ---
    consulta = _queryset_filtrado(request)
    data = [] 
    legends = []
    #-----------------
    if tipo == 'analisis':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(manejosuelo__analisis=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                '¿Realiza análisis de fertilidad del suelo', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'practica':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(manejosuelo__practica=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                                 '¿Realiza práctica de conservación de suelo', return_json=True,
                                 type = grafos.PIE_CHART_2D)
    else:
        raise Http404
    

@session_required
def grafos_ingreso(request, tipo):
    ''' tabla sobre los ingresos familiares
    '''
    #------ varaibles ------
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #-----------------------
    if tipo == 'vendio':
        for opcion in CHOICE_VENDIO:
            data.append(consulta.filter(ingresofamiliar__quien_vendio=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'A quien venden', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'maneja':
        for opcion in CHOICE_MANEJA:
            data.append(consulta.filter(ingresofamiliar__maneja_negocio=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Quien maneja negocio', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'ingreso':
        for opcion in CHOICE_MANEJA:
            data.append(consulta.filter(otrosingresos__tiene_ingreso=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Quien tiene los ingresos', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'salario':
        for opcion in TipoTrabajo.objects.all():
            sal = consulta.filter(otrosingresos__trabajo__fuente__nombre__icontains="Salarios",
                                        otrosingresos__trabajo=opcion).count()
            if sal > 0:
                data.append(sal)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de salarios', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'alquiler':
        for opcion in TipoTrabajo.objects.all():
            alqui = consulta.filter(otrosingresos__trabajo__fuente__nombre__icontains="Alquiler",
                                        otrosingresos__trabajo=opcion).count()
            if alqui > 0:
                data.append(alqui)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de alquileres', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'negocio':
        for opcion in TipoTrabajo.objects.all():
            nego = consulta.filter(otrosingresos__trabajo__fuente__nombre__icontains="Negocios",
                                        otrosingresos__trabajo=opcion).count()
            if nego > 0:
                data.append(nego)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de Negocios', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'remesa':
        for opcion in TipoTrabajo.objects.all():
            reme = consulta.filter(otrosingresos__trabajo__fuente__nombre__icontains="Remesas",
                                        otrosingresos__trabajo=opcion).count()
            if reme > 0:
                data.append(reme)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Origen de las remesas', return_json=True,
                type=grafos.PIE_CHART_2D)
    elif tipo == 'libre':
        for opcion in AquienVende.objects.all():
            data.append(consulta.filter(cultivos__venta_libre=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 'Venta libre por año', multiline = True,
                return_json = True, type = grafos.PIE_CHART_2D)
    elif tipo == 'organizada':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(cultivos__venta_organizada=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 'Venta organizada por año', multiline = True,
                return_json = True, type = grafos.PIE_CHART_2D)
    else:
        raise Http404
        
@session_required
def grafos_bienes(request, tipo):
    '''tabla de bienes'''
    #----- variables ------
    consulta = _queryset_filtrado(request)
    data = [] 
    legends = []
    #----------------------
    if tipo == 'tipocasa':
        for opcion in CHOICE_TIPO_CASA:
            data.append(consulta.filter(tipocasa__tipo=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                'Tipos de casas', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'tipopiso': 
        for opcion in Piso.objects.all():
            data.append(consulta.filter(tipocasa__piso=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                'Tipo de pisos', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'tipotecho':
        for opcion in Techo.objects.all():
            data.append(consulta.filter(tipocasa__techo=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends, 
                'Tipos de Techos', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'ambiente':
        for opcion in CHOICE_AMBIENTE:
            data.append(consulta.filter(detallecasa__ambientes=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
               'Numeros de ambientes', return_json = True,
               type = grafos.PIE_CHART_2D)
    elif tipo == 'letrina':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(detallecasa__letrina=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Tiene letrina', return_json = True,
                type = grafos.PIE_CHART_2D)
    elif tipo == 'lavadero':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(detallecasa__lavadero=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
               'Tiene lavadero', return_json = True,
               type = grafos.PIE_CHART_2D)
            
    else:
        raise Http404
            
#Tabla Organizacion Gremial
@session_required
def gremial(request):
    '''tabla de organizacion gremial'''
     #***********Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #***********************************
    
    tabla_gremial = {}
    divisor = a.aggregate(divisor=Count('organizaciongremial__socio'))['divisor']
    
    for i in OrgGremiales.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        query = a.filter(organizaciongremial__socio = i)
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__socio'))['frecuencia']     
        porcentaje = saca_porcentajes(frecuencia,divisor)
        tabla_gremial[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}
    
    #desde gremial
    tabla_desde = {}
    divisor1 = a.aggregate(divisor1=Count('organizaciongremial__desde_socio'))['divisor1']    
    for k in CHOICE_DESDE:
        key = slugify(k[1]).replace('-','_')
        query = a.filter(organizaciongremial__desde_socio = k[0])
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__desde_socio'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor1)
        tabla_desde[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}
     
 
        
    return render_to_response('organizacion/gremial.html', locals(),
                                 context_instance=RequestContext(request))
                                 
#-------------------------------------------------------------------------------
#Tabla Organizacion comunitaria
@session_required
def comunitario(request):
    ''' tablas organización comunitaria '''
    #***********Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #***********************************
    
    #rangos
    uno = a.filter(organizacioncomunitaria__numero__range=(1,5)).count()
    dos = a.filter(organizacioncomunitaria__numero__range=(6,10)).count()
    tres = a.filter(organizacioncomunitaria__numero__gt=11).count()
    
    tabla_pertenece = {}
    divisor = a.filter(organizacioncomunitaria__pertence__in=[1,2]).count()    
    for t in CHOICE_OPCION:
        key = slugify(t[1]).replace('-','_')
        query = a.filter(organizacioncomunitaria__pertence = t[0])
        frecuencia = query.aggregate(frecuencia=Count('organizacioncomunitaria__pertence'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor)
        tabla_pertenece[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}    
    
    
        
    return render_to_response('organizacion/comunitario.html', locals(),
                                context_instance=RequestContext(request) )
#-------------------------------------------------------------------------------
#aca van grafos de tenencia
                          
#Tabla Uso Tierra
@session_required
def fincas(request):
    '''Tabla de fincas'''

    tabla = {}
    totales = {}
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    
    suma = 0
    total_manzana = 0
    por_num = 0
    por_man = 0
    
    for total in Uso.objects.exclude(id=1):
        conteo = consulta.filter(usotierra__tierra = total)
        suma += conteo.count()
        man = conteo.aggregate(area = Sum('usotierra__area'))['area']
        try:
            total_manzana += man
        except:
            total_manzana = 0

    totales['numero'] = suma
    totales['manzanas'] = round(total_manzana,0)
    try:
        totales['promedio_manzana'] = round(totales['manzanas'] / consulta.count(),2)
    except:
        pass

    for uso in Uso.objects.exclude(id=1):
        key = slugify(uso.nombre).replace('-', '_')
        query = consulta.filter(usotierra__tierra = uso)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, num_familias)
        por_num += porcentaje_num
        manzanas = query.aggregate(area = Sum('usotierra__area'))['area']
        porcentaje_mz = saca_porcentajes(manzanas, totales['manzanas'])
        por_man += porcentaje_mz
        
        tabla[key] = {'numero': numero, 'porcentaje_num': porcentaje_num,
                      'manzanas': manzanas, 'porcentaje_mz': porcentaje_mz}
               
    totales['porcentaje_numero'] = por_num
    totales['porcentaje_manzana'] = round(por_man)                  
    #calculando los promedios
    lista = []
    cero = 0
    rango1 = 0
    rango2 = 0
    rango3 = 0
    rango4 = 0
    for x in consulta:
        query = UsoTierra.objects.filter(encuesta=x, tierra=1).aggregate(AreaSuma=Sum('area'))
        lista.append([x.id,query])

    for nose in lista:
        if nose[1]['AreaSuma'] == 0:
            cero += 1
        if nose[1]['AreaSuma'] >= 0.1 and  nose[1]['AreaSuma'] <= 10:
            rango1 += 1
        if nose[1]['AreaSuma'] >= 11 and nose[1]['AreaSuma'] <= 25:
            rango2 += 1
        if nose[1]['AreaSuma'] >= 26 and nose[1]['AreaSuma'] <= 50:
            rango3 += 1
        if nose[1]['AreaSuma'] >=51:
            rango4 += 1
    total_rangos = cero + rango1 + rango2 + rango3 + rango4
    por_cero = round(saca_porcentajes(cero,total_rangos),2)
    por_rango1 = round(saca_porcentajes(rango1,total_rangos),2)
    por_rango2 = round(saca_porcentajes(rango2,total_rangos),2)
    por_rango3 = round(saca_porcentajes(rango3,total_rangos),2)
    por_rango4 = round(saca_porcentajes(rango4,total_rangos),2)
    total_porcentajes = round((por_cero + por_rango1 + por_rango2 + por_rango3 + por_rango4),1)

    
    return render_to_response('reforestacion/fincas.html', 
                              locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
@session_required
def agua_restrincion(request):
    #--- variables ---
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    #------------------------------
    tabla = {}
    for agua in AguaAcceso.objects.all():
        key = slugify(agua.nombre).replace('-','_')
        query = consulta.filter(accesoagua__nombre = agua)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia,num_familias)
        tabla[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia}
        
    return render_to_response('tierra/accesoagua.html', locals(),
                               context_instance=RequestContext(request))

@session_required
def sistematizacion(request):
    #--- variables ---
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    #------------------------------
    tabla = {}
    for observaciones in Observacion.objects.all():
        key = slugify(observaciones.nombre).replace('-','_')
        query = consulta.filter(accesoagua__nombre = observaciones)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia,num_familias)
        tabla[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia}
        
    return render_to_response('agroecologico/sistematizacion.html', locals(),
                               context_instance=RequestContext(request))      
        
        
@session_required
def arboles_grafos(request, tipo):
    ''' graficos para los distintos tipos de arboles en las fincas
        Maderables, Forrajero, Energetico y Frutal
    '''
    #--- variables ---
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #-----------------
    if tipo == 'maderable':
        for opcion in Maderable.objects.all():
            madera = consulta.filter(existenciaarboles__maderable=opcion).count()
            if madera > 1:
                data.append(madera)
                legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipo Maderable', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'forrajero':
        for opcion in Forrajero.objects.all():
            forrajero = consulta.filter(existenciaarboles__forrajero=opcion).count()
            if forrajero > 1:
                data.append(forrajero)
                legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipo Forrajero', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'energetico':
        for opcion in Energetico.objects.all():
            energia = consulta.filter(existenciaarboles__energetico=opcion).count()
            if energia > 1:
                data.append(energia)
                legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
               'Tipo Energetico', return_json = True,
               type = grafos.PIE_CHART_3D)
    elif tipo == 'frutal':
        for opcion in Frutal.objects.all():
            frutal = consulta.filter(existenciaarboles__frutal=opcion).count()
            if frutal > 1:
                data.append(frutal)
                legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
               'Tipo Frutal', return_json = True,
               type = grafos.PIE_CHART_3D)
    else:
        raise Http404
        
#Tabla Existencia Arboles
@session_required
def arboles(request):
    '''Tabla de arboles'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #********Existencia de arboles sumatorias*****************
    maderable = a.aggregate(Sum('existenciaarboles__cantidad_maderable'))['existenciaarboles__cantidad_maderable__sum']
    forrajero = a.aggregate(Sum('existenciaarboles__cantidad_forrajero'))['existenciaarboles__cantidad_forrajero__sum']
    energetico = a.aggregate(Sum('existenciaarboles__cantidad_energetico'))['existenciaarboles__cantidad_energetico__sum']
    frutal = a.aggregate(Sum('existenciaarboles__cantidad_frutal'))['existenciaarboles__cantidad_frutal__sum']
    #*********************************************

    #*******promedios de arboles por familia*********
    pro_maderable = maderable / num_familias if maderable != None else 0
    pro_forrajero = forrajero / num_familias if forrajero != None else 0
    pro_energetico = energetico / num_familias if energetico != None else 0
    pro_frutal = frutal / num_familias if frutal != None else 0
    #***********************************************

    #******conteo de arboles********************
    maderablect = a.aggregate(Count('existenciaarboles__cantidad_maderable'))['existenciaarboles__cantidad_maderable__count']
    forrajeroct = a.aggregate(Count('existenciaarboles__cantidad_forrajero'))['existenciaarboles__cantidad_forrajero__count']
    energeticoct = a.aggregate(Count('existenciaarboles__cantidad_energetico'))['existenciaarboles__cantidad_energetico__count']
    frutalct = a.aggregate(Count('existenciaarboles__cantidad_frutal'))['existenciaarboles__cantidad_frutal__count']
    
    #**********Reforestacion************************
    tabla = {}
    totales = {}
    totales['numero'] = a.aggregate(numero = Count('reforestacion__reforestacion'))['numero']
    totales['porcentaje_nativos'] = 100
    totales['nativos'] = a.aggregate(nativo=Sum('reforestacion__cantidad'))['nativo']

    
    for activ in Actividad.objects.all():
        key = slugify(activ.nombre).replace('-', '_')
        query = a.filter(reforestacion__reforestacion = activ)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, num_familias)
        nativos = query.aggregate( cantidad = Sum('reforestacion__cantidad'))['cantidad']   
        totalnn = nativos
        porcentaje_nativos = saca_porcentajes(nativos, totalnn)
       
        tabla[key] = {'numero': numero, 'porcentaje_num':porcentaje_num, 
                      'porcentaje_nativos': porcentaje_nativos,'nativos': nativos 
                      }
        
    
    return  render_to_response('reforestacion/arboles.html',
                               locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla Animales en la finca
@session_required
def animales(request):
    '''Los animales y la produccion'''
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    tabla_animales = []
    #tabla_produccion = []
    
    for animal in Animales.objects.all():
        query = consulta.filter(animalesfinca__animales = animal)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, num_familias, False)
        tabla_animales.append([animal.nombre,numero,porcentaje_num])


    return render_to_response('animales/animales.html', 
                              locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla Cultivos
@session_required
def cultivos(request):
    '''tabla los cultivos y produccion'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()

    #**********calculosdelasvariables*****
    tabla = {} 
    for i in TipoCultivos.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        key2 = slugify(i.unidad).replace('-', '_')
        query = a.filter(cultivos__cultivo = i)
        area = query.aggregate(area=Sum('cultivos__area'))['area']
        totales = query.aggregate(total=Sum('cultivos__total'))['total']
        consumo = query.aggregate(consumo=Sum('cultivos__consumo'))['consumo']
        precio = query.aggregate(precio=Avg('cultivos__precio'))['precio']
        if totales > 0:
            tabla[key] = {'key2':key2,'area':area,'totales':totales,
                          'consumo':consumo,'precio':precio}
                      
    tabla_patio = {}
    for i in Patio.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        query = a.filter(cultivos__cultivo = i)
#        area = query.aggregate(area=Sum('cultivos__area'))['area']
        totales = query.aggregate(total=Sum('cultivos__total'))['total']
        consumo = query.aggregate(consumo=Sum('cultivos__consumo'))['consumo']
        precio = query.aggregate(precio=Avg('cultivos__precio'))['precio']
        if totales > 0:
            tabla_patio[key] = {'totales':totales,
                                'consumo':consumo,'precio':precio}
    
    return render_to_response('cultivos/cultivos.html',
                             locals(),
                             context_instance=RequestContext(request))
#-------------------------------------------------------------------------------

#tabla cultivos pastos
@session_required
def pastos(request):
    ''' Cultivos de pastos '''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************************
    tabla = {}
    for pasto in Pastos.objects.all():
        key = slugify(pasto.nombre).replace('-', '_')
        query = a.filter(cultivopasto__tipo = pasto)
        frecuencia = query.count()
        area = query.aggregate(area=Sum('cultivopasto__area'))['area']
        tabla[key] = {'frecuencia':frecuencia,'area':area}
         
    return render_to_response('cultivos/pastos.html', locals(), 
                               context_instance=RequestContext(request))
    

#tabla opciones de manejo                               
@session_required                               
def opcionesmanejo(request):
    '''Opciones de manejo agroecologico'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    tabla = {}
    
    for k in ManejoAgro.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(opcionesmanejo__uso = k)
        frecuencia = query.count()
        nada = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=1).aggregate(nada=Count('opcionesmanejo__nivel'))['nada']
        por_nada = saca_porcentajes(nada, num_familia)
        poco = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=2).aggregate(poco=Count('opcionesmanejo__nivel'))['poco']
        por_poco = saca_porcentajes(poco, num_familia)
        algo = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=3).aggregate(algo=Count('opcionesmanejo__nivel'))['algo']
        por_algo = saca_porcentajes(algo, num_familia)
        bastante = query.filter(opcionesmanejo__uso=k,
                                opcionesmanejo__nivel=4).aggregate(bastante=Count('opcionesmanejo__nivel'))['bastante']
        por_bastante = saca_porcentajes(bastante, num_familia)
        
        tabla[key] = {'nada':nada,'poco':poco,'algo':algo,'bastante':bastante,
                      'por_nada':por_nada,'por_poco':por_poco,'por_algo':por_algo,
                      'por_bastante':por_bastante}
    tabla_escala = {}                 
    for u in ManejoAgro.objects.all():
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(opcionesmanejo__uso = u)
        frecuencia = query.count()
        menor_escala = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__menor_escala=1).aggregate(menor_escala=
                                    Count('opcionesmanejo__menor_escala'))['menor_escala']
        menor_escala2 = query.filter(opcionesmanejo__uso=u,
                                     opcionesmanejo__menor_escala=2).aggregate(menor_escala2=
                                     Count('opcionesmanejo__menor_escala'))['menor_escala2']
        total_menor = menor_escala + menor_escala2
        por_menor_escala = saca_porcentajes(menor_escala,num_familia)
        
        # vamos ahora con la mayor escala
        
        mayor_escala = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__mayor_escala=1).aggregate(mayor_escala=
                                    Count('opcionesmanejo__mayor_escala'))['mayor_escala']
        mayor_escala2 = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__mayor_escala=2).aggregate(mayor_escala2=
                                    Count('opcionesmanejo__mayor_escala'))['mayor_escala2']
        total_mayor = mayor_escala + mayor_escala2
        por_mayor_escala = saca_porcentajes(mayor_escala, num_familia)
        tabla_escala[key] = {'menor_escala':menor_escala,'menor_escala2':menor_escala2,
                             'mayor_escala':mayor_escala,'mayor_escala2':mayor_escala2,
                             'por_menor_escala':por_menor_escala,'por_mayor_escala':por_mayor_escala}
                             
                                          
    return render_to_response('agroecologico/manejo_agro.html',locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#tabla procesamiento y comercializacion de la produccion
@session_required
def procesamiento(request):
    #--- variables ---
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    #------------------------------
    tabla = {}
    for pro in Procesado.objects.all():
        key = slugify(pro.nombre).replace('-','_')
        query = consulta.filter(procesamiento__producto = pro)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia,num_familias)
        cantidad = query.aggregate(cantidad=Sum('procesamiento__cantidad'))['cantidad']
        comer = query.aggregate(comer=Sum('procesamiento__comercializada'))['comer']
        tabla[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia,
                      'cantidad':cantidad, 'comer':comer}
        
    return render_to_response('suelo/procesamiento.html', locals(),
                               context_instance=RequestContext(request))
    

#Tabla Ahorro
@session_required
def ahorro_credito(request):
    ''' ahorro y credito'''
    #ahorro
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()
    tabla_ahorro = []
    totales_ahorro = {}

    columnas_ahorro = ['Si', '%']

    for pregunta in AhorroPregunta.objects.all():
        #opciones solo si
        subquery = consulta.filter(ahorro__ahorro = pregunta, ahorro__respuesta = 1).count()
        tabla_ahorro.append([pregunta.nombre, subquery, saca_porcentajes(subquery, consulta.count(), False)])

    #credito
    tabla_credito= {}
    totales_credito= {}

    totales_credito['numero'] = consulta.count()
    totales_credito['porcentaje_num'] = 100

    recibe = consulta.filter(credito__recibe = 1).count()
    menos = consulta.filter(credito__desde = 1).count()
    mas = consulta.filter(credito__desde = 2).count()
    al_dia = consulta.filter(credito__dia= 1).count()

    tabla_credito['recibe'] = [recibe, saca_porcentajes(recibe, totales_credito['numero'])]
    tabla_credito['menos'] = [menos, saca_porcentajes(menos, totales_credito['numero'])]
    tabla_credito['mas'] = [mas, saca_porcentajes(mas, totales_credito['numero'])]
    tabla_credito['al_dia'] = [al_dia, saca_porcentajes(al_dia, totales_credito['numero'])]

    dicc = {'tabla_ahorro':tabla_ahorro, 'columnas_ahorro': columnas_ahorro,
            'totales_ahorro': totales_ahorro, 'tabla_credito': tabla_credito,
            'num_familias': consulta.count()}

    return render_to_response('credito_ahorro/ahorro_credito.html', locals(),
                              context_instance=RequestContext(request))
#ahorro y credito
@session_required
def ahorro_credito_grafos(request, tipo):
    '''Tipo puede ser: ahorro, uso, origen, satisfaccion'''
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    if tipo == 'ahorro': #ahorra a nombre de quien
        #choice_ahorro (5, hombre), (6, mujeres), (7,ambos)
        for numero in (5, 6, 7):
            #FIX: numero de la pregunta hardcored
            dato = consulta.filter(ahorro__ahorro=5, ahorro__respuesta = numero).count()
            data.append(dato)
            legends.append(CHOICE_AHORRO[numero - 1][1])
        return grafos.make_graph(data, legends,
                'A nombre de quien ahorra', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'origen': #de donde viene el credito
        for origen in DaCredito.objects.all():
            data.append(consulta.filter(credito__quien_credito= origen).count())
            legends.append(origen.nombre)
        return grafos.make_graph(data, legends,
                'Origen del Crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'satisfaccion':
        for opcion in CHOICE_SATISFACCION:
            data.append(consulta.filter(credito__satisfaccion=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Nivel de satisfacción con el crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'uso':
        for uso in OcupaCredito.objects.all():
            data.append(consulta.filter(credito__ocupa_credito = uso).count())
            legends.append(uso.nombre)
        return grafos.make_graph(data, legends,
                'Uso del Crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    else:
        raise Http404
#tabla suelos                               
@session_required
def suelos(request):
    '''Uso del suelos'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    tabla_textura = {}
    
    #caracteristicas del terrenos
    for k in Textura.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(suelo__textura = k)
        frecuencia = query.count()
        textura = query.filter(suelo__textura=k).aggregate(textura=Count('suelo__textura'))['textura']
        por_textura = saca_porcentajes(textura, num_familia)
        tabla_textura[key] = {'textura':textura,'por_textura':por_textura}
        
    #profundidad del terrenos
    tabla_profundidad = {}
    
    for u in Profundidad.objects.all():
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(suelo__profundidad = u)
        frecuencia = query.count()
        profundidad = query.filter(suelo__profundidad=u).aggregate(profundidad=Count('suelo__profundidad'))['profundidad']
        por_profundidad = saca_porcentajes(profundidad, num_familia)
        tabla_profundidad[key] = {'profundidad':profundidad,'por_profundidad':por_profundidad}
        
    #profundidad del lombrices
    tabla_lombrices = {}
    
    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__lombrices = j)
        frecuencia = query.count()
        lombrices = query.filter(suelo__lombrices=j).aggregate(lombrices=Count('suelo__lombrices'))['lombrices']
        por_lombrices = saca_porcentajes(lombrices, num_familia)
        tabla_lombrices[key] = {'lombrices':lombrices,'por_lombrices':por_lombrices}

     #Densidad
    tabla_densidad = {}
    
    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__densidad = j)
        frecuencia = query.count()
        densidad = query.filter(suelo__densidad=j).aggregate(densidad=Count('suelo__densidad'))['densidad']
        por_densidad = saca_porcentajes(densidad, num_familia)
        tabla_densidad[key] = {'densidad':densidad,'por_densidad':por_densidad}
        
      #Pendiente
    tabla_pendiente = {}
    
    for j in Pendiente.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__densidad = j)
        frecuencia = query.count()
        pendiente = query.filter(suelo__pendiente=j).aggregate(pendiente=Count('suelo__pendiente'))['pendiente']
        por_pendiente = saca_porcentajes(pendiente, num_familia)
        tabla_pendiente[key] = {'pendiente':pendiente,'por_pendiente':por_pendiente}
        
      #Drenaje
    tabla_drenaje = {}
    
    for j in Drenaje.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__drenaje = j)
        frecuencia = query.count()
        drenaje = query.filter(suelo__drenaje=j).aggregate(drenaje=Count('suelo__drenaje'))['drenaje']
        por_drenaje = saca_porcentajes(drenaje, num_familia)
        tabla_drenaje[key] = {'drenaje':drenaje,'por_drenaje':por_drenaje}
        
    #Materia
    tabla_materia = {}
    
    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__materia = j)
        frecuencia = query.count()
        materia = query.filter(suelo__materia=j).aggregate(materia=Count('suelo__materia'))['materia']
        por_materia = saca_porcentajes(materia, num_familia)
        tabla_materia[key] = {'materia':materia,'por_materia':por_materia}
        
    return render_to_response('suelo/suelos.html',locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#tabla manejo de suelo
@session_required        
def manejosuelo(request):
    ''' Manejo del suelos'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    
    #Terrenos
    tabla_terreno = {}
    for j in Preparar.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__preparan = j)
        frecuencia = query.count()
        preparan = query.filter(manejosuelo__preparan=j).aggregate(preparan=Count('manejosuelo__preparan'))['preparan']
        por_preparan = saca_porcentajes(preparan, num_familia)
        tabla_terreno[key] = {'preparan':preparan,'por_preparan':por_preparan}
        
    #Tracción
    tabla_traccion = {}
    for j in Traccion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__traccion = j)
        frecuencia = query.count()
        traccion = query.filter(manejosuelo__traccion=j).aggregate(traccion=Count('manejosuelo__traccion'))['traccion']
        por_traccion = saca_porcentajes(traccion, num_familia)
        tabla_traccion[key] = {'traccion':traccion,'por_traccion':por_traccion}
        
    #Fertilización
    tabla_fertilizacion = {}
    for j in Fertilizacion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__fertilizacion = j)
        frecuencia = query.count()
        fertilizacion = query.filter(manejosuelo__fertilizacion=j).aggregate(fertilizacion=Count('manejosuelo__fertilizacion'))['fertilizacion']
        por_fertilizacion = saca_porcentajes(fertilizacion, num_familia)
        tabla_fertilizacion[key] = {'fertilizacion':fertilizacion,
                                    'por_fertilizacion':por_fertilizacion}
                                    
    #Tipo obra de conservación del suelo
    tabla_obra = {}
    for j in Conservacion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__obra = j)
        frecuencia = query.count()
        obra = query.filter(manejosuelo__obra=j).aggregate(obra=Count('manejosuelo__obra'))['obra']
        por_obra = saca_porcentajes(obra, num_familia)
        tabla_obra[key] = {'obra':obra,'por_obra':por_obra}
        
    return render_to_response('suelo/manejo_suelo.html',locals(),
                               context_instance=RequestContext(request))  
#-------------------------------------------------------------------------------
#Tabla Ingreso familiar y otros ingresos

#--------------------calculo de los ingresos
def calculo_cultivo(request,tipo):
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #********** calculos de los ingreso de los productos de los animales ************
    tabla = {}
    for cultivo in TipoCultivos.objects.filter(tipo=tipo):
        key = slugify(cultivo.nombre).replace('-','_')
        key2 = slugify(cultivo.unidad).replace('-','_')
        consulta = a.filter(cultivos__cultivo = cultivo)
        numero = consulta.count()
        total = consulta.aggregate(total=Sum('cultivos__total'))['total'] 
        consumo = consulta.aggregate(consumo=Sum('cultivos__consumo'))['consumo']
        try:
            cantidad = total - consumo
        except:
            pass
        precio = consulta.aggregate(precio=Avg('cultivos__precio'))['precio']
        try:
            ingreso = precio * cantidad
        except:
            ingreso = 0
        if ingreso > 0:
            tabla[key] = {'key2':key2,'numero':numero,'cantidad':cantidad,
                          'ingreso':ingreso,'precio':precio}
    return tabla

def calculo_animal(request):
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #********** calculos de los ingreso de los productos de los animales ************
    tabla = {}
    for producto in ProductoAnimal.objects.all():
        key = slugify(producto.nombre).replace('-','_')
        key2 = slugify(producto.unidad).replace('-','_')
        consulta = a.filter(produccionconsumo__producto = producto)
        numero = consulta.count()
        total = consulta.aggregate(total=Sum('produccionconsumo__total_produccion'))['total'] 
        consumo = consulta.aggregate(consumo=Sum('produccionconsumo__consumo'))['consumo']
        try:
            cantidad = total - consumo
        except:
            pass
        precio = consulta.aggregate(precio=Avg('produccionconsumo__precio'))['precio']
        try:
            ingreso = precio * cantidad
        except:
            ingreso = 0
        if ingreso > 0:
            tabla[key] = {'key2':key2,'numero':numero,'cantidad':cantidad,
                          'ingreso':ingreso,'precio':precio}
    return tabla
        
@session_required
def ingresos(request):
    '''tabla de ingresos'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #*******calculos de las variables ingreso************
    respuesta = {}
    respuesta['bruto'] = 0
    respuesta['ingreso_otro'] = 0
    respuesta['total_neto'] = 0
    #******** cultivos finca 
    agro = calculo_cultivo(request,1)
    forestal = calculo_cultivo(request,2)
    grano_basico = calculo_cultivo(request,3)
    patio = calculo_cultivo(request,5)
    frutas = calculo_cultivo(request,6)
    musaceas = calculo_cultivo(request,7)
    raices = calculo_cultivo(request,8)
    
    total_agro = 0
    c_agro = 0
    for k,v in agro.items():
        total_agro += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_agro += 1
    total_forestal = 0
    c_forestal = 0
    for k,v in forestal.items():
        total_forestal += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_forestal += 1
    total_basico = 0
    c_basico = 0
    for k,v in grano_basico.items():
        total_basico += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_basico += 1
    total_patio = 0
    c_patio = 0
    for k,v in patio.items():
        total_patio += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_patio += 1
    total_fruta = 0
    c_fruta = 0
    for k,v in frutas.items():
        total_fruta += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_fruta += 1
    total_musaceas = 0
    c_musaceas = 0
    for k,v in musaceas.items():
        total_musaceas += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_musaceas += 1
    total_raices = 0
    c_raices = 0
    for k,v in raices.items():
        total_raices += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_raices += 1

    respuesta['ingreso'] = total_agro + total_forestal + total_basico + total_patio + total_fruta + total_musaceas + total_raices
    grafo = []
    grafo.append({'Agroforestales':int(total_agro),'Forestales':int(total_forestal),
                  'Granos_basicos':int(total_basico),
                  'Animales_de_patio':int(total_patio),'Hortalizas_y_frutas':int(total_fruta),
                  'Musaceas':int(total_musaceas),'Tuberculos_y_raices':int(total_raices)
                 })
                 
    cuantos = []
    cuantos.append({'Agroforestales':c_agro,'Forestales':c_forestal,'Granos_basicos':c_basico,
                  'Animales_de_patio':c_patio,
                  'Hortalizas_y_frutas':c_fruta,'Musaceas':c_musaceas,
                  'Tuberculos_y_raices':c_raices})
   
        
    #********* calculos de las variables de otros ingresos******
    matriz = {}
    ingresototal = 0
    for j in Fuente.objects.all():
        key = slugify(j.nombre).replace('-','_')
        consulta = a.filter(otrosingresos__trabajo = j)
        frecuencia = consulta.count()
        meses = consulta.aggregate(meses=Sum('otrosingresos__meses'))['meses']
        ingreso = consulta.aggregate(ingreso=Avg('otrosingresos__Ingreso'))['ingreso']
        try:
            ingresototal = meses * ingreso
        except:
            pass
        respuesta['ingreso_otro'] +=  ingresototal
        matriz[key] = {'frecuencia':frecuencia,'meses':meses,
                       'ingreso':ingreso,'ingresototal':ingresototal}
                       
    try:
        respuesta['bruto'] = round((respuesta['ingreso'] + respuesta['ingreso_otro']) / num_familias,2)
    except:
        pass
    respuesta['total_neto'] = round(respuesta['bruto'] * 0.6,2)
        
    return render_to_response('ingresos/ingreso.html',
                              locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
                         #bienes
#-------------------------------------------------------------------------------
# Tabla equipo, infrestructura, herramientas y medio de transporte
@session_required
def equipos(request):
    '''tabla de equipos'''
    #******** variables globales***********
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #*************************************
    
    #********** tabla de equipos *************
    tabla = {}
    totales = {}
    
    totales['numero'] = a.aggregate(numero=Count('propiedadequipo__equipo'))['numero']
    totales['porciento_equipo'] = 100
    totales['cantidad_equipo'] = a.aggregate(cantidad=Sum('propiedadequipo__cantidad'))['cantidad']
    totales['porciento_cantidad'] = 100
    
    for i in Equipos.objects.all():
        key = slugify(i.nombre).replace('-','_')
        query = a.filter(propiedadequipo__equipo = i)
        frecuencia = query.count()
        por_equipo = saca_porcentajes(frecuencia, num_familia)
        equipo = query.aggregate(equipo=Sum('propiedadequipo__cantidad'))['equipo']
        cantidad_pro = query.aggregate(cantidad_pro=Avg('propiedadequipo__cantidad'))['cantidad_pro']
        tabla[key] = {'frecuencia':frecuencia, 'por_equipo':por_equipo,
                      'equipo':equipo,'cantidad_pro':cantidad_pro}
    
    #******** tabla de infraestructura *************
    tabla_infra = {}
    totales_infra = {}
    
    totales_infra['numero'] = a.aggregate(numero=Count('propiedadinfra__infraestructura'))['numero']
    totales_infra['porciento_infra'] = 100
    totales_infra['cantidad_infra'] = a.aggregate(cantidad_infra=Sum('propiedadinfra__cantidad'))['cantidad_infra']
    totales_infra['por_cantidad_infra'] = 100
       
    for j in Infraestructuras.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(propiedadinfra__infraestructura = j)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        infraestructura = query.aggregate(infraestructura=Sum('propiedadinfra__cantidad'))['infraestructura']
        infraestructura_pro = query.aggregate(infraestructura_pro=Avg('propiedadinfra__cantidad'))['infraestructura_pro']
        tabla_infra[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia,
                             'infraestructura':infraestructura,
                             'infraestructura_pro':infraestructura_pro}
                             
    #******************* tabla de herramientas ***************************
    herramienta = {}
    totales_herramientas = {}
    
    totales_herramientas['numero'] = a.aggregate(numero=Count('herramientas__herramienta'))['numero']
    totales_herramientas['porciento_herra'] = 100
    totales_herramientas['cantidad_herra'] = a.aggregate(cantidad=Sum('herramientas__numero'))['cantidad']
    totales_herramientas['porciento_herra'] = 100
    
    for k in NombreHerramienta.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(herramientas__herramienta = k)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        herra = query.aggregate(herramientas=Sum('herramientas__numero'))['herramientas']
        por_herra = query.aggregate(por_herra=Avg('herramientas__numero'))['por_herra']
        herramienta[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia,
                            'herra':herra,'por_herra':por_herra}
                            
    #*************** tabla de transporte ***********************
    transporte = {}
    totales_transporte = {}
    
    totales_transporte['numero'] = a.aggregate(numero=Count('transporte__transporte'))['numero']
    totales_transporte['porciento_trans'] = 100
    totales_transporte['cantidad_trans'] = a.aggregate(cantidad=Sum('transporte__numero'))['cantidad']
    totales_transporte['porciento_trans'] = 100
    
    for m in NombreTransporte.objects.all():
        key = slugify(m.nombre).replace('-','_')
        query = a.filter(transporte__transporte = m)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        trans = query.aggregate(transporte=Sum('transporte__numero'))['transporte']
        por_trans = query.aggregate(por_trans=Avg('transporte__numero'))['por_trans']
        transporte[key] = {'frecuencia':frecuencia,'por_frecuencia':por_frecuencia,
                           'trans':trans,'por_trans':por_trans}
                           
    electro = {}
    for m in Electro.objects.all():
        key = slugify(m.nombre).replace('-','_')
        query = a.filter(electrodomestico__electro = m)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        trans = query.aggregate(transporte=Sum('electrodomestico__cantidad'))['transporte']
        por_trans = query.aggregate(por_trans=Avg('electrodomestico__cantidad'))['por_trans']
        electro[key] = {'frecuencia':frecuencia,'por_frecuencia':por_frecuencia,
                           'trans':trans,'por_trans':por_trans}
                           
    sana = {}
    for m in Sanamiento.objects.all():
        key = slugify(m.nombre).replace('-','_')
        query = a.filter(sana__electro = m)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        trans = query.aggregate(transporte=Sum('sana__cantidad'))['transporte']
        por_trans = query.aggregate(por_trans=Avg('sana__cantidad'))['por_trans']
        sana[key] = {'frecuencia':frecuencia,'por_frecuencia':por_frecuencia,
                           'trans':trans,'por_trans':por_trans}
           
    return render_to_response('bienes/equipos.html', locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#Tabla seguridad alimentaria
def alimentos(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}

    for u in Alimentos.objects.filter(componete=numero):
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(seguridad__alimento = u)
        frecuencia = query.count()
        producen = query.filter(seguridad__alimento=u,seguridad__producen=1).aggregate(producen=Count('seguridad__producen'))['producen']
        por_producen = saca_porcentajes(producen, num_familia)
        compran = query.filter(seguridad__alimento=u,seguridad__compran=1).aggregate(compran=Count('seguridad__compran'))['compran']
        por_compran = saca_porcentajes(compran, num_familia)
        consumen = query.filter(seguridad__alimento=u,seguridad__consumen=1).aggregate(consumen=Count('seguridad__consumen'))['consumen']
        por_consumen = saca_porcentajes(consumen, num_familia)
        invierno = query.filter(seguridad__alimento=u,seguridad__consumen_invierno=1).aggregate(invierno=Count('seguridad__consumen_invierno'))['invierno']
        por_invierno = saca_porcentajes(invierno, num_familia)
        tabla[key] = {'frecuencia':frecuencia, 'producen':producen, 'por_producen':por_producen,
                      'compran':compran,'por_compran':por_compran,'consumen':consumen,
                      'por_consumen':int(por_consumen), 'invierno':invierno,
                      'por_invierno':int(por_invierno)}
    return tabla


@session_required
def seguridad_alimentaria(request):
    '''Seguridad Alimentaria'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************

    carbohidrato = alimentos(request,1)
    grasa = alimentos(request,2)
    minerales = alimentos(request,3)
    proteinas = alimentos(request,4)
    lista = []
    carbo = 0
    for k,v in carbohidrato.items():
        if v['producen'] > 0:
            carbo += 1

    gra = 0
    for k,v in grasa.items():
        if v['producen'] > 0:
            gra += 1

    mine = 0
    for k,v in minerales.items():
        if v['producen'] > 0:
            mine += 1

    prot = 0
    for k,v in proteinas.items():
        if v['producen'] > 0:
            prot += 1
    lista.append({'Carbohidratos':carbo,'Grasas':gra,'Minerales/Vitaminas':mine,'Proteínas':prot})

    return render_to_response('seguridad/seguridad.html',locals(),
                               context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#tabla uso de semilla
@session_required
def usosemilla(request):
    '''Uso de Semilla'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    tabla = {}
    lista = []
    for k in Variedades.objects.all():
        key = slugify(k.variedad).replace('-','_')
        key2 = slugify(k.cultivo.cultivo).replace('-','_')
        query = a.filter(semilla__cultivo = k )
        frecuencia = query.count()
        frec = query.filter(semilla__cultivo=k).count()
        porce = saca_porcentajes(frec,num_familia)
        nativos = query.filter(semilla__cultivo=k,semilla__origen=1).aggregate(nativos=Count('semilla__origen'))['nativos']
        introducidos = query.filter(semilla__cultivo=k,semilla__origen=2).aggregate(introducidos=Count('semilla__origen'))['introducidos']
        suma_semilla = nativos + introducidos
        por_nativos = saca_porcentajes(nativos, suma_semilla)
        por_introducidos = saca_porcentajes(introducidos, suma_semilla)

        lista.append([key,key2,frec,porce,nativos,por_nativos,
                      introducidos,por_introducidos])

        tabla[key] = {'key2':key2,'frec':frec,'porce':porce,'nativos':nativos,'introducidos':introducidos,
                      'por_nativos':por_nativos,'por_introducidos':por_introducidos}

    return render_to_response('cultivos/semilla.html',locals(),
                              context_instance=RequestContext(request))


#tabla finca vulnerable
def graves(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    suma = 0
    for p in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=p).count()
        suma += fenomeno
        
    lista = []
    for x in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=x).count()
        porcentaje = round(saca_porcentajes(fenomeno,suma),2)
        lista.append([x.nombre,fenomeno,porcentaje])        
    return lista
    
def suma_graves(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    suma = 0
    for p in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=p).count()
        suma += fenomeno
    return suma

@session_required
def vulnerable(request):
    ''' Cuales son los Riesgos que hace las fincas vulnerables '''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    
    #fenomenos naturales
    sequia = graves(request,1)
    total_sequia = suma_graves(request,1)
    inundacion = graves(request,2)
    total_inundacion = suma_graves(request,2)
    vientos = graves(request,3)
    total_vientos = suma_graves(request,3)
    deslizamiento = graves(request,4)
    total_deslizamiento = suma_graves(request,4)
    
    #Razones agricolas
    falta_semilla = graves(request,5)
    total_falta_semilla = suma_graves(request,5)
    mala_semilla = graves(request,6)
    total_mala_semilla = suma_graves(request,6)
    plagas = graves(request,7)
    total_plagas = suma_graves(request,7)
    
    #Razones de mercado
    bajo_precio = graves(request,8)
    total_bajo_precio = suma_graves(request,8)
    falta_venta = graves(request,9)
    total_falta_venta = suma_graves(request,9)
    estafa = graves(request,10)
    total_estafa = suma_graves(request,10)
    falta_calidad = graves(request,11)
    total_falta_calidad = suma_graves(request,11)
    
    #inversion
    falta_credito = graves(request,12)
    total_falta_credito = suma_graves(request,12)
    alto_interes = graves(request,13)
    total_alto_interes = suma_graves(request,13)
    
    tabla = {}
    lista2 = []
    for i in Fenomeno.objects.all():
        key = slugify(i.nombre).replace('-','_')
        key2 = slugify(i.causa.nombre).replace('-','_')
        query = a.filter(vulnerable__motivo = i)
        frecuencia = query.count()
        porce = saca_porcentajes(frecuencia,num_familia)
        
        lista2.append([key,key2,frecuencia,porce])
    
    return render_to_response('riesgos/vulnerable.html',locals(),
                              context_instance=RequestContext(request))
#-------------------------------------------------------------------------------
#tabla mitigacion de riesgos
@session_required    
def mitigariesgos(request):
    ''' Mitigación de los Riesgos '''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************
    tabla = {}
    for j in PreguntaRiesgo.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(riesgos__pregunta = j)
        mitigacion = query.filter(riesgos__pregunta=j, riesgos__respuesta=1).aggregate(mitigacion=Count('riesgos__pregunta'))['mitigacion']
        por_mitigacion = saca_porcentajes(mitigacion, num_familia)
        tabla[key] = {'mitigacion':mitigacion,'por_mitigacion':por_mitigacion}
        
    return render_to_response('riesgos/mitigacion.html',locals(),
                               context_instance=RequestContext(request)) 
#-------------------------------------------------------------------------------
#tabla participacion de la familia en labores, beneficios y toma de decisiones
def participacion(request):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************************    
    labores = {}
    for especie in Rubros.objects.all():
        key = slugify(especie.nombre).replace('-','_')
        labores[key] = {}
        for decide in Decision.objects.all():
            cuanto = a.filter(participasion__rubro=especie, participasion__labores=decide).count()
            labores[key][decide.nombre] = cuanto
            
    beneficio = {}
    for especie in Rubros.objects.all():
        key = slugify(especie.nombre).replace('-','_')
        beneficio[key] = {}
        for decide in Decision.objects.all():
            cuanto = a.filter(participasion__rubro=especie, participasion__beneficios=decide).count()
            beneficio[key][decide.nombre] = cuanto
            
    deciciones = {}
    for especie in Rubros.objects.all():
        key = slugify(especie.nombre).replace('-','_')
        deciciones[key] = {}
        for decide in Decision.objects.all():
            cuanto = a.filter(participasion__rubro=especie, participasion__decision=decide).count()
            deciciones[key][decide.nombre] = cuanto
            
    return render_to_response('participacion/participa.html', locals(),
                               context_instance=RequestContext(request))    

    
#-------------------------------------------------------------------------------    
#Los puntos en el mapa
def obtener_lista(request):
    if request.is_ajax():
        lista = []
        for objeto in Encuesta.objects.all():
            dicc = dict(nombre=objeto.entrevistado, id=objeto.id, 
                        lon=float(objeto.comunidad.municipio.longitud), 
                        lat=float(objeto.comunidad.municipio.latitud)
                        )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

#-------------------------------------------------------------------------------
# Aca empieza el menu para los subindicadores :)
                               
@session_required
def familia(request):
    '''Familias: aca van las familias con sus respectivos indicadores, educacion,
       salud, energia, agua.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('encuestas/familia.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))
                              
@session_required
def organizacion(request):
    '''Organizacion: aca van las organizaciones con sus respectivos indicadores,
       como son gremial y comunitaria.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('organizacion/organizacion.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))
                              
@session_required
def riesgo(request):
    '''Riesgos: aca van los riesgos con sus indicadores como son: vulnerabilidad 
       en la finca asi como la mitigación de estos.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('riesgos/riesgos.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))
                              
@session_required
def suelo(request):
    '''Suelo: aca va el indicador de suelo con sus subindicadores: caracteristicas
       del terrreno y manejo del suelo
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('suelo/suelo.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))
                              
@session_required
def tenencias(request):
    '''Tenencia: aca van las tenencias con sus respectivos subindicadores: 
       tenencia de la propiedad, documento legal, tierra etc.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('encuestas/tenencia.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))
                              
@session_required
def tierra(request):
    '''Tierra: aca va el indicador uso de tierra con su respectivos subindicadores:
       uso de la tierra, existencia de arboles y reforestacion.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('tierra/tierra.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))                                   
#TODO: completar esto
VALID_VIEWS = {
        'educacion': educacion,
        'salud': salud,
        'luz':luz,
        'agua': agua,
        'pastos': pastos,
        'fincas':fincas,
        'arboles': arboles,
        'animales': animales,
        'cultivos': cultivos,
        'ingresos': ingresos,
        'equipos': equipos,
        'riesgo': riesgo,
        'tierra': tierra,
        'suelo': suelo,
        'suelos': suelos,
        'familia': familia,
        'gremial': gremial,
        'tenencias': tenencias,
        'usosemilla': usosemilla,
        'vulnerable': vulnerable,
        'manejosuelo': manejosuelo,
        'comunitario' : comunitario,
        'organizacion': organizacion,
        'mitigariesgos': mitigariesgos,
        'ahorro_credito': ahorro_credito,
        'opcionesmanejo': opcionesmanejo,
        'seguridad': seguridad_alimentaria,
        'participacion': participacion,
        'restrincion': agua_restrincion,
        'sistematizacion': sistematizacion,
        'procesamiento': procesamiento,
        'general': generales,
         
  }
        
# Vistas para obtener los municipios, comunidades, etc..

def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
    
#def get_organizacion(request, departamento):
#    encuestas = Encuesta.objects.filter(municipio__departamento=departamento)    
#    organizaciones = OrganizacionOCB.objects.filter(encuesta__in=encuestas).distinct()
#    lista = [(organizacion.id, organizacion.nombre) for organizacion in organizaciones]
#    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def get_comunidad(request, municipio):
    comunidades = Comunidad.objects.filter(municipio = municipio )
    lista = [(comunidad.id, comunidad.nombre) for comunidad in comunidades]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
    
# Funciones utilitarias para cualquier proposito

def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores_cero = [] #lista para anotar los indices en los que da cero el porcentaje
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        values[i] = "%.2f" % porcentaje + '%' 
    return values

def saca_porcentajes(dato, total, formato=True):
    '''Si formato es true devuelve float caso contrario es cadena'''
    if dato != None:
        try:
            porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else: 
        return 0

def calcular_positivos(suma, numero, porcentaje=True):
    '''Retorna el porcentaje de positivos'''
    try:
        positivos = (numero * 2) - suma
        if porcentaje:
            return '%.2f' % saca_porcentajes(positivos, numero)
        else:
            return positivos
    except:
        return 0

def calcular_negativos(suma, numero, porcentaje = True):
    positivos = calcular_positivos(suma, numero, porcentaje)
    if porcentaje:
        return 100 - float(positivos)
    else:
        return numero - positivos  
