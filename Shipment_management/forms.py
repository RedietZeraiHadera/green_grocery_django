from django import forms
from .models import Shipment

class ShipmentUPloadForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = "__all__"
        
