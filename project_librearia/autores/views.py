from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AutorModel
from .serializers import AutorSerializer

# Función para formato de respuesta uniforme
def response_format(success=True, message="", data=None, count=None, http_status=status.HTTP_200_OK):
    response = {
        "status": success,
        "message": message,
        "data": data,
    }
    if count is not None:
        response["count"] = count
    return Response(response, status=http_status)

class AutorApiView(APIView):
    def get(self, request):
        autores = AutorModel.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return response_format(
            message="Lista de autores",
            data=serializer.data,
            count=autores.count(),
            http_status=status.HTTP_200_OK
        )
    
    def post(self, request):
        serializer = AutorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response_format(
                message="Autor creado exitosamente",
                data=serializer.data,
                http_status=status.HTTP_201_CREATED
            )
        return response_format(
            success=False,
            message="Error de validación",
            data=serializer.errors,
            http_status=status.HTTP_400_BAD_REQUEST
        )

class AutorApiViewDetail(APIView):
    def get_object(self, id):
        try:
            return AutorModel.objects.get(pk=id)
        except AutorModel.DoesNotExist:
            return None

    def get(self, request, id):
        autor = self.get_object(id)
        if autor is None:
            return response_format(
                success=False,
                message="Autor no encontrado",
                http_status=status.HTTP_404_NOT_FOUND
            )
        serializer = AutorSerializer(autor)
        return response_format(
            message="Detalle del autor",
            data=serializer.data,
            http_status=status.HTTP_200_OK
        )

    def put(self, request, id):
        autor = self.get_object(id)
        if autor is None:
            return response_format(
                success=False,
                message="Autor no encontrado",
                http_status=status.HTTP_404_NOT_FOUND
            )
        serializer = AutorSerializer(autor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response_format(
                message="Autor actualizado exitosamente",
                data=serializer.data,
                http_status=status.HTTP_200_OK
            )
        return response_format(
            success=False,
            message="Error de validación",
            data=serializer.errors,
            http_status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        autor = self.get_object(id)
        if autor is None:
            return response_format(
                success=False,
                message="Autor no encontrado",
                http_status=status.HTTP_404_NOT_FOUND
            )
        autor.delete()
        return response_format(
            message="Autor eliminado exitosamente",
            data=None,
            http_status=status.HTTP_204_NO_CONTENT
        )
