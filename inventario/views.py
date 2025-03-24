from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, Movimiento
from .forms import MovimientoForm

@login_required
def lista_productos(request):
    """
    Muestra la lista de productos y permite registrar movimientos.
    """
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Movimiento registrado con éxito.')
                return redirect('lista_productos')
            except ValueError as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos.')
    else:
        form = MovimientoForm()
    
    context = {
        'productos': productos,
        'form': form,
        'titulo': 'Lista de Productos'
    }
    return render(request, 'inventario/lista_productos.html', context)

@login_required
def historial_movimientos(request):
    """
    Muestra el historial de movimientos ordenados por fecha descendente.
    """
    movimientos = Movimiento.objects.all().order_by('-fecha')
    context = {
        'movimientos': movimientos,
        'titulo': 'Historial de Movimientos'
    }
    return render(request, 'inventario/historial_movimientos.html', context)