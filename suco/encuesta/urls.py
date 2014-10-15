from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
#from models import Encuesta

urlpatterns = patterns('suco.encuesta.views',
    #(r'^index/$', 'inicio'),
    (r'^menu/$', 'menu'),
    (r'^nuevos_informes/(?P<grupo>\w+)/(?P<numero_encuesta>\w+)/(?P<indicador>\w+)', 'nuevos_informes'),
    (r'^general/$', 'generales'),
    #(r'^ajax/organizaciones/(?P<departamento>\d+)/$', 'get_organizacion'),
    (r'^ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    #graficas para los indicadores
    (r'^grafo/organizacion/(?P<tipo>\w+)/$', 'organizacion_grafos'),
    (r'^grafo/agua-disponibilidad/(?P<tipo>\d+)/$', 'agua_grafos_disponibilidad'),
    (r'^grafo/fincas/(?P<tipo>\w+)/$', 'fincas_grafos'),
    (r'^grafo/arboles/(?P<tipo>\w+)/$', 'arboles_grafos'),
    (r'^grafo/manejosuelo/(?P<tipo>\w+)/$', 'grafo_manejosuelo'),
    (r'^grafo/ingreso/(?P<tipo>\w+)/$', 'grafos_ingreso'),
    (r'^grafo/bienes/(?P<tipo>\w+)/$', 'grafos_bienes'),
    (r'^grafo/ahorro-credito/(?P<tipo>\w+)/$', 'ahorro_credito_grafos'),
    (r'^mapa/$', 'obtener_lista'),

    #(r'^ayuda/$',   direct_to_template,{'template': 'acerca.html'}),
    (r'^acerca/$',   direct_to_template,{'template': 'acerca.html'}),

    (r'^(?P<vista>\w+)/$', '_get_view'),
      
)
