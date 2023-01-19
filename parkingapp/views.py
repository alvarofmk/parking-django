from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms.forms import FacturacionForm, AbonadoForm
from django.shortcuts import render
import random
import pdb;
from datetime import timedelta
from django.shortcuts import redirect


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

def gestionAbonados(request):
    listaAbonados = []
    
    if request.method == 'POST':
        form = FacturacionForm(request.POST)
        if form.is_valid():
            pass
    else:
        ultimos = request.GET.get('ultimos', '')
        if ultimos == 'true':
            listaAbonados = Abonado.objects.filter(fechaCancelacion__gte=timezone.now()).filter(fechaCancelacion__lte=timezone.now() + timedelta(days=10))
        else:
            listaAbonados = Abonado.objects.all()
    return render(request, 'admin/abonados.html', {
        'listaAbonados': listaAbonados,
    })

def formularioAbonado(request, matricula):
    form = AbonadoForm()
    if request.method == 'POST':
        form = AbonadoForm(request.POST)
        if form.is_valid():
            
            fechaCan = timezone.now() + timedelta(days=form.cleaned_data['tipoAbono'].duracion*30)
            tiposPlaza = TipoPlaza.objects.get(pk=form.cleaned_data['tipoVehiculo'])
            plazas = Plaza.objects.filter(estado='LI').all()
    
            noEncontrado = True
            i=0

            while i < len(plazas) and noEncontrado:
                if plazas[i].tipoPlaza == tiposPlaza:
                    noEncontrado = False
                    plaza = plazas[i]

            newAbonado =Abonado(form.cleaned_data['matricula'],
            form.cleaned_data['tipoVehiculo'],
            form.cleaned_data['dni'],
            form.cleaned_data['nombre'],
            form.cleaned_data['apellidos'],
            form.cleaned_data['email'],
            form.cleaned_data['tarjeta'],
            timezone.now(),
            fechaCan,
            True,
            random.randint(100000, 999999),
            plaza,
            form.cleaned_data['matricula'],
            form.cleaned_data['tipoAbono']
            )
            
            newAbonado.save()
            plaza.estado=Plaza.estadoChoices.ABONOLIBRE
            plaza.save()

    return render(request, 'admin/formAbonados.html', {
        'form' : form,
    })

def avisoBaja(request, matricula):
    abonado = Abonado.objects.get(pk=matricula)
    template = loader.get_template('admin/baja.html')
    context = {
        'abonado': abonado
    }
    return HttpResponse(template.render(context))

def bajaAbonado(request, matricula):
    abonado = Abonado.objects.get(pk=matricula)
    abonado.activo = False
    abonado.plaza.estado = Plaza.estadoChoices.LIBRE
    abonado.fechaCancelacion = timezone.now()
    abonado.save()
    abonado.plaza.save()
    return redirect(gestionAbonados)

def caducidadAbonados(request):
    return HttpResponse()