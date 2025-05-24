from rest_framework import serializers
from .models import AutorModel

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorModel
        fields = '__all__'
        read_only_fields = ('usuario_creador', 'fecha_creacion', 'fecha_modificacion')

    def create(self, validated_data):
        usuario = self.context['request'].user if 'request' in self.context else None
        return AutorModel.objects.create(usuario_creador=usuario, **validated_data)

    def update(self, instance, validated_data):
        # No actualizamos usuario_creador en la edición, solo otros campos
        return super().update(instance, validated_data)
