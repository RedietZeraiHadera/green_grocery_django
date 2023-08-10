from django import forms
from .models import Cart

class CartUPloadForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
        
