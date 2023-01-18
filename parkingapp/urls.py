from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator', views.indexAdmin, name='menu-admin'),
    path('parking', views.indexUser, name='menu-user'),
    path('administrator/estado', views.estadoPlazas, name='estado'),
    path('administrator/facturacion', views.consultarFacturacion, name='facturacion'),
]