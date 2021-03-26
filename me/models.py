from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # email=models.EmailField(max_length=50,unique=True)
    # username=models.CharField(max_length=54)
    first_name=models.CharField(max_length=54)
    last_name=models.CharField(max_length=54)
    
    is_employee=models.BooleanField(default=False)

    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)    
    phone=models.CharField(max_length=54)
class Empolyee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)    
    phone=models.CharField(max_length=54)
