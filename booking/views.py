from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

# Create your views here:
def book_ing(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'booking/home.html', context)

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'booking/place_order.html', context)

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=OrderForm(instance=order)
    context = {
        'form': form
    }

    return render(request, 'booking/edit_order.html', context)

