from django.urls import path
from .views import vendor_upload_form,vendor_list,vendor_detail,edit_vendor_view



urlpatterns = [
     path('salesperson/upload', vendor_upload_form, name='vendor_upload_view'),
     path('salesperson/list', vendor_list, name='vendor_list_view'),
     path("salesperson/<int:id>/",vendor_detail,name="vendor_detail_view"),
     path("salesperson/edit/<int:id>/", edit_vendor_view, name="vendor_edit_view")


]