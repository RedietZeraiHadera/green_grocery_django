from django.shortcuts import render
from rest_framework import APIView
from customer_management.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response

# Create your views here.

class CustomerListView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many = True)
        return Response(serializers.data)
