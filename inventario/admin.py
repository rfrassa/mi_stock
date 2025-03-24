from django.contrib import admin
from .models import Categoria, Almacen, Producto, Movimiento

admin.site.register(Categoria)
admin.site.register(Almacen)
admin.site.register(Producto)
admin.site.register(Movimiento)