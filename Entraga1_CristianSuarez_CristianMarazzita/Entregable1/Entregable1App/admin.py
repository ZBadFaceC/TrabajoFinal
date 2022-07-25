from django.contrib import admin

from .models import *


class CanchaAdmin(admin.ModelAdmin):

    list_display = ('tipo', 'tamaño', 'costo', 'horario')
    search_fields = ('tipo', 'tamaño', 'costo',)


class ClienteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')

class DeporteAdmin(admin.ModelAdmin):

    list_display = ('tipo', 'profesor', 'costo')
    search_fields = ('tipo', 'profesor', 'costo')

admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Deporte, DeporteAdmin)


admin.site.register(Avatar)