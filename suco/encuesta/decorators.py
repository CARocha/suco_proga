from django.http import HttpResponseRedirect
from django.db.models.signals import post_delete
from django.db.models.signals import post_save

def session_required(f):
    def check_session(request, **kwargs):
        if 'activo' not in request.session:
            return HttpResponseRedirect('/')
        return f(request, **kwargs)
    return check_session