from django.shortcuts import render
from .models import Dish,RestaurantProfile

# Create your views here.
def restaurant_dashboard(request):
    return render(request,'restaurant_dashboard.html')

def add_dish(request):
    data=request.POST
    is_available=is_available in request.POST
    restaurant_profile=RestaurantProfile.objects.get(user=request.user)
    Dish.objects.create(name=data['name'],category=data['category'],price=data['price'],qty=data['qty'],description=data['description'],is_available=is_available,restaurant=restaurant_profile)
    all_data=Dish.objects.all()
    return render(request,)

def list_dish(request):
    data=request.POST
    all_data=Dish.objects.all()
    return render(request,)
    









    

