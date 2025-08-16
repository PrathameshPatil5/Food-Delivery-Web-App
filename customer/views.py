from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, Order, OrderItem
from restaurant.models import Dish

def customer_dashboard(request):
    return render(request, "customer_dashboard.html")

@login_required
def cart_add(request):
    if request.method == "POST":
        dish_id = request.POST.get("dish")
        quantity = int(request.POST.get("quantity", 1))
        dish = get_object_or_404(Dish, id=dish_id)
        Cart.objects.create(customer=request.user, dish=dish, quantity=quantity)
        return redirect("cart_read")
    
    dishes = Dish.objects.all()
    return render(request, "customer_browse.html", {"dishes": dishes})

@login_required
def cart_read(request):
    items = Cart.objects.filter(customer=request.user)
    
    # Calculate total_price for each item
    for item in items:
        item.total_price = item.dish.price * item.quantity
    
    return render(request, "cart_read.html", {"items": items})  # Updated template name

@login_required
def cart_update(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, customer=request.user)
    if request.method == "POST":
        item.quantity = int(request.POST.get("quantity", item.quantity))
        item.save()
        return redirect("cart_read")
    return render(request, "cart_update.html", {"item": item})

@login_required
def cart_delete(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, customer=request.user)
    if request.method == "POST":
        item.delete()
        return redirect("cart_read")
    return render(request, "cart_delete.html", {"item": item})

@login_required
def order_create(request):
    cart_items = Cart.objects.filter(customer=request.user)
    if not cart_items:
        return redirect("cart_read")
    
    total = sum(item.dish.price * item.quantity for item in cart_items)
    order = Order.objects.create(customer=request.user, total_amount=total)
    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            dish=item.dish,
            quantity=item.quantity,
            price=item.dish.price
        )
    
    cart_items.delete()
    return redirect("order_read")

@login_required
def order_read(request):
    orders = Order.objects.filter(customer=request.user).prefetch_related('items')
    return render(request, "order_read.html", {"orders": orders})

@login_required
def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    if request.method == "POST":
        order.status = request.POST.get("status", order.status)
        order.save()
        return redirect("order_read")
    return render(request, "order_update.html", {"order": order})

@login_required
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    if request.method == "POST":
        order.delete()
        return redirect("order_read")
    return render(request, "order_delete.html", {"order": order})
