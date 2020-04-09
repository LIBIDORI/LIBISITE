from django.contrib import admin

# Register your models here.

from .models import Provincia,Municipio,Socio,Incidencia,ReciboDevuelto

admin.site.register(Provincia)
#admin.site.register(Municipio)
#admin.site.register(Socio)

#Define the admin class

class MunicipioAdmin(admin.ModelAdmin):
    list_display=('nombremunicipiocastellano','nombremunicipiolenguaoficial','cprovincia')

# Register the admin class with the associated model
admin.site.register(Municipio,MunicipioAdmin)


class SocioAdmin(admin.ModelAdmin):
    list_display=('apellidos','nombre','nif_nie','numero','cprovincia','cmunicipio','fecha_alta','fecha_baja')

admin.site.register(Socio,SocioAdmin)

class IncidenciaAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','descripcion','estado','observaciones')

admin.site.register(Incidencia,IncidenciaAdmin)

class ReciboDevueltoAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','referencia','titular','iban','importe','motivo')

admin.site.register(ReciboDevuelto,ReciboDevueltoAdmin)