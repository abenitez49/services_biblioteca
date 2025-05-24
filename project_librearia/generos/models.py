# generos/models.py
from django.db import models
from utils.models import AuditoriaModel

class GeneroModel(AuditoriaModel):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "generos"
        ordering = ['id']

    def __str__(self):
        return self.nombre
