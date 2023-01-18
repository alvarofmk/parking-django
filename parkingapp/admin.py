from django.contrib import admin
from .models import Abonado, Cliente, Ocupa, Plaza, TipoAbono, TipoPlaza

admin.site.register(Abonado)
admin.site.register(Cliente)
admin.site.register(Ocupa)
admin.site.register(Plaza)
admin.site.register(TipoAbono)
admin.site.register(TipoPlaza)


# Register your models here.
