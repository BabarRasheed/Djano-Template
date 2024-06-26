from django import forms
from .models import CheckoutInformation

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutInformation
        fields = [       
            "first_name",
            "last_name",
            "company_name",
            "area_code",
            "primary_phone",
            "street_address_1",
            "street_address_2",
            "zip_code",
        ]

