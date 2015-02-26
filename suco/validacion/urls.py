from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^validacion/(?P<centroid>\d+)/(?P<grupoid>\d+)/$', 'suco.validacion.views.validacion_jovenlist', name="validacion_jovenlist"),
    url(r'^validacion/(?P<centroid>\d+)/$', 'suco.validacion.views.validacion_centrochosen', name="validacion_centrochosen"),
    url(r'^validacion/$', 'suco.validacion.views.validacion', name="validacion"),
    url(r'^validacion_save_joven_comment/$', 'suco.validacion.views.validacion_save_joven_comment', name="validacion_save_joven_comment"),
)
