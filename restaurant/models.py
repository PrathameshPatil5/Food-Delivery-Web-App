from django.db import models
from accounts.models import Customuser

# Create your models here.
class RestaurantProfile(models.Model):
    user=models.OneToOneField(Customuser,on_delete=models.CASCADE) 
    restaurant_name=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    contact_number=models.CharField(max_length=255)
    opening_hours=models.IntegerField(blank=True)

class Dish(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.IntegerField()
    qty=models.IntegerField()
    description=models.TextField(blank=True)
    is_available=models.BooleanField(default=False)
    restaurant=models.ForeignKey(RestaurantProfile,on_delete=models.CASCADE)

