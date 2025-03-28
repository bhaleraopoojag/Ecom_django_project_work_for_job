from django import forms 
from . models import AddressModel


class AddressForm(forms.ModelForm):
    class Meta:
        model=AddressModel
        fields=[
            # 'billing_profile',
            # 'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'postal_code'
        ]

