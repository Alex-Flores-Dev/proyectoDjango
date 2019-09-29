from django.contrib import admin

from form.models import Solicitud,Cliente,Productos,Bancos

admin.site.register(Cliente)
admin.site.register(Solicitud)
admin.site.register(Productos)
admin.site.register(Bancos)

# Register your models here.
