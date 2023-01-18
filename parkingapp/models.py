import datetime
from django.db import models

# Create your models here.
class Cliente(models.Model):

    matricula = models.TextField(primary_key=True)
    tipoChoices = [
        ('TURISMO', 'Turismo'),
        ('MOTOCICLETA', 'Motocicleta'),
        ('MOVILIDADREDUCIDA', 'Movilidad reducidad'),
    ]
    tipo = models.CharField(max_length=50, choices=tipoChoices)

class TipoPlaza(models.Model):

    tipoChoices = [
        ('TURISMO', 'Turismo'),
        ('MOTOCICLETA', 'Motocicleta'),
        ('MOVILIDADREDUCIDA', 'Movilidad reducidad'),
    ]
    tipo =  models.CharField(max_length=50, choices=tipoChoices, primary_key=True)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2) 
    porcentajePlazas = models.DecimalField(max_digits=5, decimal_places=2) 
    numPlazas = models.IntegerField()

    def __str__(self):
        return 'Plazas reservadas para ' + self.__tipo + ' con tarificación por minuto de ' + self.__tarifa

class Plaza(models.Model):

    id = models.IntegerField(primary_key=True) 
    tipoPlaza = models.ForeignKey(TipoPlaza, on_delete=models.PROTECT)
    estadoChoices = [
        ('LIBRE', 'Libre'),
        ('OCUPADA', 'Ocupada'),
        ('ABONOLIBRE', 'Libre con abono'),
        ('ABONOOCUPADA', 'Ocupada con abono'),
    ]
    estado = models.CharField(max_length=50, choices=estadoChoices)

    def __str__(self):
        return 'Plaza con id ' + self.id + ' reservada para ' + self.tipoPlaza.tipo + ', actualmente se encuentra ' + self.estado

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
