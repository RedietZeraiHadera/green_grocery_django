from django.shortcuts import render,redirect
from .forms import VendorUPloadForm
from .models import Vendor

# Create your views here.


def vendor_upload_form(request):
    if request.method == 'POST':
        form = VendorUPloadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("customer_list") 
    else:
        form = VendorUPloadForm()
    return render(request, "vendor/vendor_upload.html", {"form": form})


def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})

def vendor_detail(request, id):
    vendors =Vendor.objects.get(id=id)
    return render(request, "vendor/vendor_detail.html", {"vendors": vendors})

def edit_vendor_view(request, id):
    vendors = Vendor.objects.get(id=id)
    if request.method == "POST":
        form = VendorUPloadForm(request.POST, request.FILES, instance=vendors)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail_view", id=id)  
    else:
        form = VendorUPloadForm(instance=vendors)
    return render(request, 'vendor/edit_vendor.html', {"form": form})
