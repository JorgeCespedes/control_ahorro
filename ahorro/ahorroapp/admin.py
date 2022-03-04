from django.contrib import admin
from . models import Detalle

# Register your models here.

class DetalleAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)

admin.site.register(Detalle, DetalleAdmin)