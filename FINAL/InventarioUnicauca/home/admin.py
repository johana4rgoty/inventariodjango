from django.contrib import admin
from.models import *

# Register your models here.

admin.site.register(Roles)
admin.site.register(Usuario)
admin.site.register(Sala)
admin.site.register(Ip)
admin.site.register(Dispositivo)
admin.site.register(PrestamoSala)
admin.site.register(PrestamoIp)
admin.site.register(PrestamoDispositivo)
admin.site.register(Elemento)