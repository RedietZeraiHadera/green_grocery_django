from django.shortcuts import render,redirect
from .forms import ShipmentUPloadForm
from .models import Shipment

# Create your views here.
def shipment_upload_form(request):
    if request.method == 'POST':
        form = ShipmentUPloadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shipment_list")  # Redirect to the customer list view after successful form submission
    else:
        form = ShipmentUPloadForm()
    return render(request, "shipment/shipment_upload.html", {"form": form})


def shipment_list(request):
    shipments = Shipment.objects.all()
    return render (request, "shipment/shipment_list.html", {"shipments": shipments})


def shipment_detail(request,id):
    shipments = Shipment.objects.get(id=id)
    return render (request, "shipment/shipment_detail.html", {"shipments" :shipments})



def edit_shipment_view(request,id):
    shipments= Shipment.objects.get(id=id)
    if request.method =="POST":
        form = ShipmentUPloadForm(request.POST, instance=shipments)
        if form.is_valid():
            form.save()
            return redirect("shipment_detail_view", id = shipments.id)

    else:
        form = ShipmentUPloadForm(instance=shipments)

    return render(request, 'shipment/edit_shipment.html',{"form":form})


             
        




