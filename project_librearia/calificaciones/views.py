# clasificaciones/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CalificacionModel
from .serializers import CalificacionSerializer
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def response_format(success=True, message="", data=None, count=None, http_status=status.HTTP_200_OK):
    response = {
        "status": success,
        "message": message,
        "data": data,
    }
    if count is not None:
        response["count"] = count
    return Response(response, status=http_status)

def create_embedding(text):
    if not text:
        return None
    vector = embedding_model.encode(text)
    return vector.tolist()

class CalificacionApiView(APIView):
    def get(self, request):
        calificaciones = CalificacionModel.objects.all()
        serializer = CalificacionSerializer(calificaciones, many=True)
        return response_format(
            message="Lista de calificaciones",
            data=serializer.data,
            count=calificaciones.count(),
            http_status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = CalificacionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            descripcion = serializer.validated_data.get('descripcion', '')
            embedding_vector = create_embedding(descripcion)
            # Guardamos el embedding junto a la creación
            calificacion = serializer.save(embedding=embedding_vector)
            return response_format(
                message="Calificación creada exitosamente",
                data=CalificacionSerializer(calificacion).data,
                http_status=status.HTTP_201_CREATED
            )
        return response_format(
            success=False,
            message="Error de validación",
            data=serializer.errors,
            http_status=status.HTTP_400_BAD_REQUEST
        )

class CalificacionApiViewDetail(APIView):
    def get_object(self, id):
        try:
            return CalificacionModel.objects.get(pk=id)
        except CalificacionModel.DoesNotExist:
            return None

    def get(self, request, id):
        calificacion = self.get_object(id)
        if calificacion is None:
            return response_format(
                success=False,
                message="Calificación no encontrada",
                http_status=status.HTTP_404_NOT_FOUND
            )
        serializer = CalificacionSerializer(calificacion)
        return response_format(
            message="Detalle de la calificación",
            data=serializer.data,
            http_status=status.HTTP_200_OK
        )

    def put(self, request, id):
        calificacion = self.get_object(id)
        if calificacion is None:
            return response_format(
                success=False,
                message="Calificación no encontrada",
                http_status=status.HTTP_404_NOT_FOUND
            )
        serializer = CalificacionSerializer(calificacion, data=request.data, context={'request': request})
        if serializer.is_valid():
            descripcion = serializer.validated_data.get('descripcion', '')
            embedding_vector = create_embedding(descripcion)
            calificacion = serializer.save(embedding=embedding_vector)
            return response_format(
                message="Calificación actualizada exitosamente",
                data=CalificacionSerializer(calificacion).data,
                http_status=status.HTTP_200_OK
            )
        return response_format(
            success=False,
            message="Error de validación",
            data=serializer.errors,
            http_status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        calificacion = self.get_object(id)
        if calificacion is None:
            return response_format(
                success=False,
                message="Calificación no encontrada",
                http_status=status.HTTP_404_NOT_FOUND
            )
        calificacion.delete()
        return response_format(
            message="Calificación eliminada exitosamente",
            data=None,
            http_status=status.HTTP_204_NO_CONTENT
        )
