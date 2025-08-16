from django.db import models
from accounts.models import Customuser

class RestaurantProfile(models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)  # FIXED

    def __str__(self):
        return self.restaurant_name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)   # FIXED
    qty = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.restaurant.restaurant_name})"
