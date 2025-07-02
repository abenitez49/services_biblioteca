from rest_framework import serializers
from .models import CalificacionModel

class CalificacionSerializer(serializers.ModelSerializer):
    libro_nombre = serializers.CharField(source='id_libro_fk.nombre', read_only=True)
    usuario_creador_username = serializers.CharField(source='usuario_creador.username', read_only=True)

    class Meta:
        model = CalificacionModel
        fields = [
            'id',
            'valor',
            'descripcion',
            'id_libro_fk',
            'libro_nombre',
            'usuario_creador_username',
            'usuario_creador',
            'fecha_creacion',
            'fecha_modificacion'
        ]
        read_only_fields = ['usuario_creador', 'fecha_creacion', 'fecha_modificacion']
        
    def validate(self, data):
        user = self.context['request'].user
        libro = data.get('id_libro_fk')

        if CalificacionModel.objects.filter(usuario_creador=user, id_libro_fk=libro).exists():
            raise serializers.ValidationError(
                {"detalle": "Ya has calificado este libro."}
            )

        return data

    def create(self, validated_data):
        usuario = self.context['request'].user if 'request' in self.context else None
        return CalificacionModel.objects.create(usuario_creador=usuario, **validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
