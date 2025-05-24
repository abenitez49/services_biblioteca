# autores/models.py
from django.db import models
from utils.models import AuditoriaModel

class AutorModel(AuditoriaModel):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "autores"
        ordering = ['id']

    def __str__(self):
        return self.nombre
