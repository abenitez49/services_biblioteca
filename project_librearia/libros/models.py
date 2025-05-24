import os
from django.db import models
from utils.models import AuditoriaModel
from autores.models import AutorModel
from generos.models import GeneroModel

def libro_epub_path(instance, filename):
    # Si la instancia ya tiene id, usarlo para la carpeta
    if instance.id:
        return f'libros_epub/{instance.id}/{filename}'
    else:
        # Si no tiene id aún (nuevo registro), guardamos en carpeta temporal
        return f'libros_epub/temp/{filename}'

class LibrosModel(AuditoriaModel):
    nombre = models.CharField(max_length=100)
    id_genero_fk = models.ForeignKey(GeneroModel, on_delete=models.CASCADE, db_column='id_genero_fk')
    id_autor_fk = models.ForeignKey(AutorModel, on_delete=models.CASCADE, db_column='id_autor_fk')
    fecha_lanzamiento = models.DateField()
    archivo = models.FileField(upload_to=libro_epub_path, null=True, blank=True)

    class Meta:
        db_table = "libros"
        ordering = ['id']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

