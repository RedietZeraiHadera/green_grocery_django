from django.contrib import admin
# Register your models here.
from.models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display= ("name","quantity","total","date_created","deliverymethod")
admin.site.register(Shipment,ShipmentAdmin)


