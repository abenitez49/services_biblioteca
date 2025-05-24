from django.urls import path
from .views import CalificacionApiView, CalificacionApiViewDetail

urlpatterns = [
    path('', CalificacionApiView.as_view(), name='calificaciones'),
    path('/<int:id>', CalificacionApiViewDetail.as_view(), name='calificaciones-detail'),
]
