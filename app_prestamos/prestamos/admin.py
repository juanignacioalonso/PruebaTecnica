from django.contrib import admin
from prestamos import models



class Admin(admin.ModelAdmin):
    list_display = ('nombre',)  # Campos que se mostrarán en la lista de objetos

# Registra el modelo con la configuración personalizada en la página de administración
admin.site.register(models.Genero, Admin)

class Usuario(admin.ModelAdmin):
    list_display=('email',)

admin.site.register(models.MiUsuario, Usuario)