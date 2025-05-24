from django.db import models
from django.contrib.auth import get_user_model

class AuditoriaModel(models.Model):
    usuario_creador = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
