from django.urls import path
from .views import GeneroApiView, GeneroApiViewDetail

urlpatterns = [
    path('', GeneroApiView.as_view(), name='generos'),
    path('/<int:id>', GeneroApiViewDetail.as_view(), name='generos-detail'),
]
