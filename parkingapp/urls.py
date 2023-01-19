from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator', views.indexAdmin, name='menu-admin'),
    path('parking', views.indexUser, name='menu-user'),
    path('administrator/estado', views.estadoPlazas, name='estado'),
    path('administrator/facturacion', views.consultarFacturacion, name='facturacion'),
    path('administrator/abonados', views.gestionAbonados, name='abonados'),
    path('administrator/abonados/formulario', views.formularioAbonado, name='abonados-alta'),
    path('administrator/abonados/formulario/<slug:matricula>', views.formularioAbonado, name='abonados-modificacion'),
    path('administrator/abonados/baja/<slug:matricula>', views.bajaAbonado, name='abonados-baja'),
]