from rest_framework import serializers
from .models import AutorModel

class AutorSerializer(serializers.ModelSerializer):
    usuario_creador_username = serializers.CharField(source='usuario_creador.username', read_only=True)

    class Meta:
        model = AutorModel
        fields = [
            'id',
            'nombre',
            'fecha_creacion',
            'fecha_modificacion',
            'usuario_creador_username'
        ]
        read_only_fields = ('usuario_creador', 'fecha_creacion', 'fecha_modificacion')

    def create(self, validated_data):
        usuario = self.context['request'].user if 'request' in self.context else None
        return AutorModel.objects.create(usuario_creador=usuario, **validated_data)

    def update(self, instance, validated_data):
        # No actualizamos usuario_creador en la edición, solo otros campos
        return super().update(instance, validated_data)
