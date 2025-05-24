from django.urls import path
from libros.views import LibrosApiView, LibrosApiViewDetail
from libros.views import  lista_libros


urlpatterns = [
    path('v1/libros', LibrosApiView.as_view()),
    path('v1/libros/<int:id>', LibrosApiViewDetail.as_view()),
    path('libros/', lista_libros, name='lista_libros'),

]