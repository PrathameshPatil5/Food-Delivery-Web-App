from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Customuser
from restaurant.models import RestaurantProfile

def register_view(request):
    if request.method == 'POST':
        data = request.POST
        user = Customuser.objects.create_user(
            username=data['username'],
            password=data['password'],
            role=data['role']
        )

        if data['role'] == 'restaurant':
            RestaurantProfile.objects.create(
                user=user,
                restaurant_name=data.get('restaurant_name', 'Unnamed Restaurant'),
                address=data.get('address', 'No address yet'),
                contact_number=data.get('contact_number', ''),
                opening_hours=data.get('opening_hours') or None
            )

        return redirect('login')
    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.role == 'customer':
                return redirect('customer_dashboard')
            elif user.role == 'restaurant':
                return redirect('restaurant_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
