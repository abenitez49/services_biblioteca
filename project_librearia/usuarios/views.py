from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Validar si el nombre de usuario ya existe
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso.")
        
        # Crear el usuario
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Esto permite el acceso sin autenticación

    def create(self, request, *args, **kwargs):
        # Llamamos al método create() de la vista para crear el usuario
        response = super().create(request, *args, **kwargs)

        # Retornamos una respuesta con un mensaje de éxito (puedes incluir más datos si es necesario)
        return Response({
            "message": "Usuario registrado con éxito",
            "user": response.data
        }, status=status.HTTP_201_CREATED)
