from django.db import models
from payment_management.models import Payment

# Create your models here.

class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=32)
    payment_method = models.CharField(max_length=50)
    delivery_method = models.CharField(max_length=50,default="standard shipping")
    shipping_address = models.TextField(default='')
    total = models.DecimalField(max_digits=10,decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
   

    def __str__(self):
        return self.name
