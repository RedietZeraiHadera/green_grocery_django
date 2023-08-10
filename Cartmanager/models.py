from django.db import models
from inventory.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    product = models.CharField(max_length=32)
    total = models.FloatField()
    number_of_products = models.PositiveIntegerField()
    shipping_cost = models.FloatField()
    payment_options = models.CharField(max_length=20)
    discount = models.FloatField()

    def __str__(self):
        return self.product







