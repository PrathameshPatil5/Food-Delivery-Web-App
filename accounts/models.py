from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.\
choices=[
    ("restaurant","restaurant"),
    ("customer","customer")
]
class Customuser(AbstractUser):
    role=models.CharField(max_length=255,choices=choices)
    
