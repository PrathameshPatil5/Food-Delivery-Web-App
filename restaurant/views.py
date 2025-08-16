from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dish, RestaurantProfile

@login_required
def restaurant_dashboard(request):
    return render(request, "restaurant_dashboard.html")

@login_required
def add_dish(request):
    restaurant_profile = get_object_or_404(RestaurantProfile, user=request.user)
    if request.method == "POST":
        data = request.POST
        Dish.objects.create(
            name=data.get("name"),
            category=data.get("category"),
            price=data.get("price"),
            qty=data.get("qty"),
            description=data.get("description"),
            is_available="is_available" in data,
            restaurant=restaurant_profile
        )
        return redirect("restaurant_list")
    return render(request, "restaurant_add.html")

@login_required
def list_dish(request):
    restaurant_profile = get_object_or_404(RestaurantProfile, user=request.user)
    dishes = Dish.objects.filter(restaurant=restaurant_profile)
    return render(request, "restaurant_list.html", {"dishes": dishes})

@login_required
def update_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id, restaurant__user=request.user)
    if request.method == "POST":
        data = request.POST
        dish.name = data.get("name")
        dish.category = data.get("category")
        dish.price = data.get("price")
        dish.qty = data.get("qty")
        dish.description = data.get("description")
        dish.is_available = "is_available" in data
        dish.save()
        return redirect("restaurant_list")
    return render(request, "restaurant_update.html", {"dish": dish})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id, restaurant__user=request.user)
    if request.method == "POST":
        dish.delete()
        return redirect("restaurant_list")
    return render(request, "restaurant_delete.html", {"dish": dish})
