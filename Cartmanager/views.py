from django.shortcuts import render, redirect
from .forms import CartUPloadForm
from .models import Cart

# Create your views here.
def cart_upload_form(request):
    if request.method == 'POST':
        form = CartUPloadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cart_list")  
    else:
        form = CartUPloadForm()
    return render(request, "cart/cart_upload.html", {"form": form})



def cart_list(request):
    carts = Cart.objects.all()
    return render(request, "cart/cart_list.html", {"carts": carts})


def cart_detail(request, id):
    carts = Cart.objects.get(id=id)
    return render(request, "cart/cart_detail.html", {"carts": carts})


def edit_cart_view(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartUPloadForm(request.POST, request.FILES, instance=cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail_view", id=id)  
    else:
        form = CartUPloadForm(instance=cart)
    return render(request, 'cart/edit_cart.html', {"form": form})







