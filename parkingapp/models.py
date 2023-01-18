import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Cliente(models.Model):

    class tipoChoices(models.TextChoices):
        TURISMO = 'TU', _('Turismo')
        MOTOCICLETA = 'MO', _('Motocicleta')
        MOVILIDADREDUCIDA = 'MR', _('Movilidad reducida')

    matricula = models.TextField(primary_key=True)
    tipo =  models.CharField(max_length=2, choices=tipoChoices.choices)

class TipoPlaza(models.Model):

    class tipoChoices(models.TextChoices):
        TURISMO = 'TU', _('Turismo')
        MOTOCICLETA = 'MO', _('Motocicleta')
        MOVILIDADREDUCIDA = 'MR', _('Movilidad reducida')

    tipo =  models.CharField(max_length=2, choices=tipoChoices.choices, primary_key=True)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2) 
    porcentajePlazas = models.DecimalField(max_digits=5, decimal_places=2) 
    numPlazas = models.IntegerField()

class Plaza(models.Model):

    class estadoChoices(models.TextChoices):
        LIBRE = 'LI', _('Libre')
        OCUPADA = 'OC', _('Ocupada')
        ABONOLIBRE = 'AL', _('Abono libre')
        ABONOOCUPADA = 'AO', _('Abono ocupada')

    id = models.IntegerField(primary_key=True) 
    tipoPlaza = models.ForeignKey(TipoPlaza, on_delete=models.PROTECT)
    estado = models.CharField(max_length=2, choices=estadoChoices.choices)

class TipoAbono(models.Model):

    nombre = models.CharField(max_length=255, primary_key=True)
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

class Abonado(Cliente):

    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField()
    tarjeta = models.CharField(max_length=255)
    fechaSuscripcion = models.DateTimeField()
    fechaCancelacion = models.DateTimeField()
    activo = models.BooleanField()
    pin = models.IntegerField()
    plaza = models.ForeignKey(Plaza, on_delete=models.PROTECT)
    tipoAbono = models.ForeignKey(TipoAbono, on_delete=models.PROTECT)

class Ocupa(models.Model):

    pin = models.IntegerField(primary_key=True)
    entrada = models.DateTimeField()
    salida = models.DateTimeField()
    activo = models.BooleanField()
    costeTotal = models.DecimalField(max_digits=5, decimal_places=2)
    plaza = models.ForeignKey(Plaza, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
