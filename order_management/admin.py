from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","total","date_ordered","total","payment_method","delivery_method","shipping_address")

admin.site.register(Order,OrderAdmin)    

