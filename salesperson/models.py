from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    contact = models.CharField(max_length=32)
    storename = models.CharField(max_length=32)
   


    def __str__(self):
        return self.name