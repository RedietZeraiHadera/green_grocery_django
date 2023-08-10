# from django.shortcuts import render,redirect
# from .forms import OrderUPloadForm
# from .models import Order

# # Create your views here.


# def order_upload_form(request):
#     if request.method == 'POST':
#         form = OrderUPloadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("order_list")  # Redirect to the customer list view after successful form submission
#     else:
#         form = OrderUPloadForm()
#     return render(request, "order/order_upload.html", {"form": form})




# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, "order/order_list.html", {"orders": orders})



# def order_detail(request, id):
#     order = Order.objects.get(id=id)
#     return render(request, "order/order_detail.html", {"customer": order})

# def edit_order_view(request, id):
#     order = Order.objects.get(id=id)
#     if request.method == "POST":
#         form = OrderUPloadForm(request.POST, request.FILES, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect("order_detail_view", id=id)  # Redirect to customer detail view after saving
#     else:
#         form = OrderUPloadForm(instance=Order)
#     return render(request, 'order/edit_order.html', {"form": form})
