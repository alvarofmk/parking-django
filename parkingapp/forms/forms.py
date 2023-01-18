from django import forms

class FacturacionForm(forms.Form):
    fechaInicio = forms.DateTimeField(label="Fecha de inicio", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    fechaFin = forms.DateTimeField(label="Fecha final", required=True, widget=forms.DateInput(attrs={'type': 'date'}))