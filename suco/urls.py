from django.conf.urls.defaults import patterns, include, url
import settings
from os import path as os_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suco.views.home', name='home'),
    # url(r'^suco/', include('suco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^', include('suco.validacion.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('suco.smart_selects.urls')),
    (r'^xls/$', 'suco.utils.save_as_xls'),
    (r'^$', 'suco.encuesta.views.index'),
    (r'^', include('suco.encuesta.urls')),
    url(r'^validacion/(?P<centroid>\d+)$', 'suco.validacion.views.validacion_centrochosen'),
)

handler404 = 'suco.views.file_not_found_404'

handler500 = 'suco.views.file_not_found_500'

urlpatterns += staticfiles_urlpatterns() 

