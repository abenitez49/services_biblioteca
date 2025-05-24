# clasificaciones/models.py
from django.db import models
from utils.models import AuditoriaModel
from libros.models import LibrosModel

class CalificacionModel(AuditoriaModel):
    valor = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=50)
    id_libro_fk = models.ForeignKey(LibrosModel, on_delete=models.CASCADE, db_column='id_libro_fk')

    class Meta:
        db_table = "calificaciones"
        ordering = ['valor']

    def __str__(self):
        return f"{self.valor} - {self.descripcion}"
