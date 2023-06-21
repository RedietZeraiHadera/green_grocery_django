from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=6,decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name
