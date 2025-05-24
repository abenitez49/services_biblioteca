from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from libros.models import LibrosModel
from libros.serializers import LibrosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

def lista_libros(request):
    libros = LibrosModel.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})

class LibrosApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # Aceptar archivos

    def get(self, request):
        libros = LibrosModel.objects.all()
        serializer = LibrosSerializer(libros, many=True)
        return Response({
            'success': True,
            'message': 'Libros obtenidos correctamente.',
            'data': serializer.data,
            'count': len(serializer.data)
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LibrosSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Libro creado correctamente.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Error al crear el libro.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class LibrosApiViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, id):
        try:
            return LibrosModel.objects.get(pk=id)
        except LibrosModel.DoesNotExist:
            return None

    def get(self, request, id):
        libro = self.get_object(id)
        if libro is None:
            return Response({
                'success': False,
                'message': 'Libro no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosSerializer(libro)
        return Response({
            'success': True,
            'message': 'Libro obtenido correctamente.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        libro = self.get_object(id)
        if libro is None:
            return Response({
                'success': False,
                'message': 'Libro no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosSerializer(libro, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Libro actualizado correctamente.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Error al actualizar el libro.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        libro = self.get_object(id)
        if libro is None:
            return Response({
                'success': False,
                'message': 'Libro no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)
        libro.delete()
        return Response({
            'success': True,
            'message': 'Libro eliminado correctamente.'
        }, status=status.HTTP_204_NO_CONTENT)
