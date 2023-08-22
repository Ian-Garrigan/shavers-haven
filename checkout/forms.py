from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    #Make the layout of the order form with class meta

    class Meta:
        """
        Manage the behaviour of the model fields
        """
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'country',
            'county',
            'postcode',
            'town_or_city',
            'street_address1',
            'street_address2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "town_or_city": "Town or City",
            "county": "County",
            "postcode": "Postcode",
            "country" : "Country",
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
