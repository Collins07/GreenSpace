# from django.shortcuts import render

# # Create your views here.
# def business(request):
#     return render (request, 'business/index.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, ShoppingCart
from .forms import OrderForm

def index(request):
    return render(request, 'index.html')

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            order, created = Order.objects.get_or_create(
                product=product,
                buyer=request.user,
                is_ordered=False,
                defaults={'quantity': quantity},
            )
            if not created:
                order.quantity += quantity
                order.save()
            messages.success(request, f"{quantity} {product.name} added to cart.")
            return redirect('cart')
    else:
        form = OrderForm()
    return render(request, 'product_detail.html', {'product': product, 'form': form})

@login_required
def cart(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    order, created = Order.objects.get_or_create(
        product=product,
        buyer=request.user,
        is_ordered=False,
        defaults={'quantity': 1},
    )
    if not created:
        order.quantity += 1
        order.save()
    cart.orders.add(order)
    messages.success(request, f"{product.name} added to cart.")
    return redirect('cart')

@login_required
def remove_from_cart(request, order_id):
    order = get_object_or_404(Order, pk=order_id, buyer=request.user, is_ordered=False)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart.orders.remove(order)
    messages.success(request, f"{order.product.name} removed from cart.")
    return redirect('cart')

@login_required
def checkout(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    orders = cart.orders.filter(is_ordered=False)
    if request.method == 'POST':
        for order in orders:
            order.is_ordered = True
            order.save()
        messages.success(request, "Order placed successfully!")
        cart.orders.clear() # clear the shopping cart after order is placed
        return redirect('products')
    total_cost = cart.get_total_cost()
    return render(request, 'checkout.html', {'orders': orders, 'total_cost': total_cost})

