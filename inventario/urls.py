from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
   # path('movimientos/', views.registrar_movimiento, name='registrar_movimiento'), antes activar debo tener la vista creada
]