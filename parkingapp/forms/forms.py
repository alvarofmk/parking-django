import enum
from django import forms
from django.utils.translation import gettext_lazy as _

from parkingapp.models import TipoAbono

class TipoChoices(enum.Enum):
    TURISMO = 'TU', _('Turismo')
    MOTOCICLETA = 'MO', _('Motocicleta')
    MOVILIDADREDUCIDA = 'MR', _('Movilidad reducida')

class FacturacionForm(forms.Form):
    fechaInicio = forms.DateTimeField(label="Fecha de inicio", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    fechaFin = forms.DateTimeField(label="Fecha final", required=True, widget=forms.DateInput(attrs={'type': 'date'}))

class AbonadoForm(forms.Form):
    matricula = forms.CharField(max_length=15, required=True)
    dni = forms.CharField(max_length=9, required=True)
    nombre = forms.CharField(max_length=255, required=True)
    apellidos = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    tarjeta = forms.CharField(max_length=255, required=True)
    tipoVehiculo = forms.ChoiceField(choices=[TipoChoices.TURISMO.value, TipoChoices.MOTOCICLETA.value, TipoChoices.MOVILIDADREDUCIDA.value], required=True)
    tipoAbono = forms.ModelChoiceField(queryset=TipoAbono.objects.all(), required=True, help_text="Tipo de abono")