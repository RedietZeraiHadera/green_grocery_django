from django.urls import path
from .views import CustomerListView




urlpatterns = [
    path("customer_management/",CustomerListView.as_view(),name = "customer_list_view")
]