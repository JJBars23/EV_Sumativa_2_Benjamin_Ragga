from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)


    class Meta:
        verbose_name_plural = "editoriales"

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "libros"

    @property
    def precio_formateado(self):
        return f"${self.precio:,.0f}"

    def __str__(self):
        return self.titulo