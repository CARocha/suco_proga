from django.shortcuts import render_to_response
from django.template import RequestContext

def file_not_found_404(request, template_name="404.html"):
    page_title = 'Recurso No Encontrado'
    return render_to_response(template_name, locals(),
                               context_instance=RequestContext(request))
                               
def file_not_found_500(request, template_name="500.html"):
    page_title = 'Error interno'
    return render_to_response(template_name, locals(),
                               context_instance=RequestContext(request))
