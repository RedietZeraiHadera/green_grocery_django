from django.contrib import admin

# Register your models here.
from .models import Product
class Product_Admin(admin.ModelAdmin):
    list_display = ("name","stock","price","date_created","description","date_updated")

admin.site.register(Product,Product_Admin)   