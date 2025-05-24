from django.urls import path
from .views import AutorApiView, AutorApiViewDetail

urlpatterns = [
    path('', AutorApiView.as_view(), name='autores-list'),
    path('/<int:id>', AutorApiViewDetail.as_view(), name='autores-detail'),
]
