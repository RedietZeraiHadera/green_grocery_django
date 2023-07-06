from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    order_number = models.PositiveIntegerField()
    status = models.TextField()
    mathod_of_payment = models.CharField(max_length=32)
    date_of_payment = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
