from django import template
register = template.Library()
from django.template.defaultfilters import floatformat

@register.filter
def restar(value, arg):
    print arg
    return int(value)-int(arg)

@register.filter
def total_dict(value):    
    return sum(value.values())

@register.filter
def total_per_key(value, arg):
    '''value es el dict y arg es el key del que se quiere obtener el total o suma'''   
    return sum([v[arg] for v in value.values()])

@register.filter
def total_general(tabla):   
    '''donde tabla es un dicc donde estan todos los valores'''
    return sum([sum(value.values()) for value in tabla.values()]) 

@register.filter
def frecuencia(cantidad, tabla):   
    '''donde cantidad es la cantidad y tabla es todos los valores del dicc'''
    total = total_general(tabla)
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / float(total)
    return int(round(x, 0))

@register.filter
def get_value(dicc, key):   
    '''donde dicc es el diccionario con valores y key la llave a obtener'''
    return dicc[key]

@register.filter
def percent(value):
    if value is None:
        return None

    if value == "":
        return ""

    value = float(value)

    if value == 0: return "n/d"
    #return floatformat(value, 2)
    return floatformat(value * 100.0, 2) + '%'

#cambia el URL del informe actual para mostrar el mismo informe solo para un joven.
@register.filter
def este_informe_con_joven(currenturl,joven):
    joven_url = currenturl.replace('auto', str(joven.id))
    return joven_url
