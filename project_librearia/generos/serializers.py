from rest_framework import serializers
from .models import GeneroModel

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = ['id', 'nombre', 'usuario_creador', 'fecha_creacion', 'fecha_modificacion']
        read_only_fields = ['usuario_creador', 'fecha_creacion', 'fecha_modificacion']

    def create(self, validated_data):
        usuario = self.context['request'].user if 'request' in self.context else None
        return GeneroModel.objects.create(usuario_creador=usuario, **validated_data)

    def update(self, instance, validated_data):
        # No actualizamos usuario_creador
        return super().update(instance, validated_data)
