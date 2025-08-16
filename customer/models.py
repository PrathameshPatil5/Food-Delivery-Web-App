from django.db import models
from accounts.models import Customuser
from restaurant.models import Dish

class Cart(models.Model):   # FIXED name to PascalCase
    customer = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"

class Order(models.Model):
    customer = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)  # FIXED name
    status = models.CharField(max_length=50, default='pending')  # FIXED lowercase
    date_created = models.DateTimeField(auto_now_add=True)       # FIXED name
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.username} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"
