from django.db import models
# Create your models here.
class Cart(models.Model):
    products = models.CharField(max_length=32)
    total = models.FloatField()
    number_of_products = models.PositiveIntegerField()
    shipping_cost = models.FloatField()
    payment_options = models.CharField(max_length=20)
    discount = models.FloatField()
    def _str_(self):
        return self.products