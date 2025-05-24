from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GeneroModel
from .serializers import GeneroSerializer

class GeneroApiView(APIView):
    def get(self, request):
        generos = GeneroModel.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response({
            'success': True,
            'message': 'Géneros obtenidos correctamente.',
            'data': serializer.data,
            'count': len(serializer.data)
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GeneroSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Género creado correctamente.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Error al crear el género.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class GeneroApiViewDetail(APIView):
    def get_object(self, id):
        try:
            return GeneroModel.objects.get(pk=id)
        except GeneroModel.DoesNotExist:
            return None

    def get(self, request, id):
        genero = self.get_object(id)
        if genero is None:
            return Response({
                'success': False,
                'message': 'Género no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = GeneroSerializer(genero)
        return Response({
            'success': True,
            'message': 'Género obtenido correctamente.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        genero = self.get_object(id)
        if genero is None:
            return Response({
                'success': False,
                'message': 'Género no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = GeneroSerializer(genero, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Género actualizado correctamente.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Error al actualizar el género.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        genero = self.get_object(id)
        if genero is None:
            return Response({
                'success': False,
                'message': 'Género no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        genero.delete()
        return Response({
            'success': True,
            'message': 'Género eliminado correctamente.'
        }, status=status.HTTP_204_NO_CONTENT)
