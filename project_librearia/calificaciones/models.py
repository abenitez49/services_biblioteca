# clasificaciones/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField  # <-- Importar ArrayField
from utils.models import AuditoriaModel
from libros.models import LibrosModel


class CalificacionModel(AuditoriaModel):
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    id_libro_fk = models.ForeignKey(LibrosModel, on_delete=models.CASCADE, db_column='id_libro_fk')

    embedding = ArrayField(models.FloatField(), blank=True, null=True)  # <-- campo nuevo

    class Meta:
        db_table = "calificaciones"
        ordering = ['valor']
        unique_together = ('usuario_creador', 'id_libro_fk')

    def __str__(self):
        return f"{self.usuario_creador} - {self.valor} - {self.descripcion}"
