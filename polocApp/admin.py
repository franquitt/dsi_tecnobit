from django.contrib import admin
from .models import *

admin.site.register(Criticidad)
admin.site.register(TipoSolicitud)
admin.site.register(Proyecto)
admin.site.register(Cliente)
admin.site.register(SolicitudMantenimiento)

# Register your models here.
