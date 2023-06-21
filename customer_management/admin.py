from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","email","password","location","contacts")

admin.site.register(Customer,CustomerAdmin)    
