from datetime import timedelta
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms.forms import FacturacionForm
from django.shortcuts import render


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def indexUser(request):
    template = loader.get_template('user/menu.html')
    return HttpResponse(template.render())

def indexAdmin(request):
    nPlazasLibres = Plaza.objects.filter(estado=Plaza.estadoChoices.LIBRE).count()
    ocupacion = (200 - nPlazasLibres) / (200/100)
    template = loader.get_template('admin/menu.html')
    context = {
        'nPlazasLibres': nPlazasLibres,
        'ocupacion' : ocupacion
    }
    return HttpResponse(template.render(context))

def estadoPlazas(request):
    plazas = Plaza.objects.all()
    template = loader.get_template('admin/plazas.html')
    context = {
        'plazas': plazas
    }
    return HttpResponse(template.render(context))

def consultarFacturacion(request):
    listaFacturacion = []
    ningunResultado = False
    if request.method == 'POST':
        form = FacturacionForm(request.POST)
        if form.is_valid():
            listaFacturacion = Ocupa.objects.filter(salida__gte=form.cleaned_data['fechaInicio']).filter(salida__lte=form.cleaned_data['fechaFin']).filter(activo=False)
            ningunResultado = not len(listaFacturacion) > 0
    else:
        form = FacturacionForm()

    return render(request, 'admin/facturacion.html', {
        'listaFacturacion': listaFacturacion,
        'form' : form,
        'ningunResultado' : ningunResultado
    })