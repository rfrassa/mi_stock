from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import MovimientoForm

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = MovimientoForm()

    return render(request, 'inventario/lista_productos.html', {
        'productos': productos,
        'form': form
    })