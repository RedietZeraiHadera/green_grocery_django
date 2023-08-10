from django.shortcuts import render, redirect
from .forms import CustomerUPloadForm
from .models import Customer

def customer_upload_form(request):
    if request.method == 'POST':
        form = CustomerUPloadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("customer_list")  # Redirect to the customer list view after successful form submission
    else:
        form = CustomerUPloadForm()
    return render(request, "customer/customer_upload.html", {"form": form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer/customer_detail.html", {"customer": customer})

def edit_customer_view(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerUPloadForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail_view", id=id)  # Redirect to customer detail view after saving
    else:
        form = CustomerUPloadForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {"form": form})
