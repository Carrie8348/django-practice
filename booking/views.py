from django.shortcuts import render, redirect
from .models import Order

# Create your views here:
def book_ing(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'booking/home.html', context)

def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('order_name')
        done = 'done' in request.POST
        Order.objects.create(name=name, done=done)

        return redirect('home')
    return render(request, 'booking/place_order.html')