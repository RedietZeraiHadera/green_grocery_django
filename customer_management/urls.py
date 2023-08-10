from .views import customer_upload_form, customer_list, customer_detail, edit_customer_view
from django.urls import path



urlpatterns =[
    path('customer_management/upload', customer_upload_form, name='customer_upload_view'),
    path('customer_management/list', customer_list, name='customer_list_view'),
    path("customer_management/<int:id>/",customer_detail,name="customer_detail_view"),
    path("customer_management/edit/<int:id>/", edit_customer_view, name="customer_edit_view")
]