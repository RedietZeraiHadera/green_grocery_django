from django.db import models
from payment_management.models import Payment
from customer_management.models import Customer
from Cartmanager.models import Cart
from Shipment_management.models import Shipment

# Create your models here.

class Order(models.Model):
    shipment = models.ManyToManyField(Shipment)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
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
