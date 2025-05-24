from rest_framework import serializers
from .models import LibrosModel

class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrosModel
        fields = [
            'id',
            'nombre',
            'id_genero_fk',
            'id_autor_fk',
            'fecha_lanzamiento',
            'archivo',  
            'usuario_creador',
            'fecha_creacion',
            'fecha_modificacion'
        ]
        read_only_fields = ['usuario_creador', 'fecha_creacion', 'fecha_modificacion']
        
    def get_archivo_url(self, obj):
        request = self.context.get('request')
        if obj.archivo and request:
            return request.build_absolute_uri(obj.archivo.url)
        return None

    def create(self, validated_data):
        usuario = self.context['request'].user if 'request' in self.context else None
        archivo = validated_data.pop('archivo', None)

        # Crear el libro sin archivo
        libro = LibrosModel.objects.create(usuario_creador=usuario, **validated_data)

        if archivo:
            libro.archivo = archivo
            libro.save()

        return libro



    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
