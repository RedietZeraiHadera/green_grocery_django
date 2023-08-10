from django.urls import path
from .views import shipment_upload_form,shipment_list,shipment_detail,edit_shipment_view


urlpatterns = [
    path("shipment_management/upload",shipment_upload_form,name="shipment_upload_view"),
    path("shipment_management/list",shipment_list,name="shipment_list_view"),
    path("shipment_management/<int:id>/",shipment_detail,name="shipment_detail_view"),
    path("shipment_management/edit/<int:id>/", edit_shipment_view, name="shipment_edit_view"),
   

]