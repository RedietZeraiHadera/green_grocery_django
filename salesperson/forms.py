from django import forms
from .models import Vendor

class VendorUPloadForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
        
