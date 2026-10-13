from django.contrib import admin
from .models import Editorial, Libro

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'direccion', 'telefono')
    search_fields = ('nombre', 'pais')
    list_filter = ('pais',)
    ordering = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'fecha_publicacion', 'precio_formateado')
    search_fields = ('titulo', 'autor')
    list_filter = ('editorial', 'fecha_publicacion')
    ordering = ('titulo',)