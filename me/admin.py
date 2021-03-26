from django.contrib import admin
from .models import Customer,User,Empolyee
# Register your models here.


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Empolyee)