from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
    ("restaurant", "Restaurant"),
    ("customer", "Customer"),
]

class Customuser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
