from django import forms
from django.db import transaction
from .models import Customer,User,Empolyee
from django.contrib.auth.forms import UserCreationForm


class Customesign(UserCreationForm):
    first_name=forms.CharField(max_length=41)
    last_name=forms.CharField(max_length=41)
    phone=forms.CharField(max_length=40)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)    
        
        user.first_name=self.cleaned_data.get('first_name')
        
        user.last_name=self.cleaned_data.get('last_name')
        user.is_customer=True
        user.save()
        customer=Customer.objects.create(user=user)
        customer.phone=self.cleaned_data.get('phone')
        customer.save()
        return user
        
class Employeesign(UserCreationForm):
    first_name=forms.CharField(max_length=41)
    last_name=forms.CharField(max_length=41)
    phone=forms.CharField(max_length=40)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)    
        
        user.first_name=self.cleaned_data.get('first_name')
        
        user.last_name=self.cleaned_data.get('last_name')
        user.is_employee=True
        user.save()
        cus=Empolyee.objects.create(user=user)
        cus.phone=self.cleaned_data.get('phone')
        cus.save()
        return user


    
