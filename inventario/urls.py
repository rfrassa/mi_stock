from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('historial/', views.historial_movimientos, name='historial_movimientos'),
]