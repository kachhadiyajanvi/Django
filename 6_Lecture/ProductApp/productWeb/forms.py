# yourapp/forms.py
from django import forms
from .models import Product   # assuming your model is named Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']   # add more fields if needed
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Wireless Mouse',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '19.99',
                'step': '0.01',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '50',
                'min': '0',
            }),
        }