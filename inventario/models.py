from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.almacen.nombre})"

class Movimiento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.producto.nombre}: {self.cantidad} el {self.fecha}"

    def save(self, *args, **kwargs):
        # Actualiza la cantidad del producto al guardar el movimiento
        self.producto.cantidad += self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)