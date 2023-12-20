from django import forms
from .models import CartItem, Product
from django.contrib.auth.models import User


class AddToCartForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects, widget=forms.HiddenInput)
    user = forms.ModelChoiceField(queryset=User.objects, widget=forms.HiddenInput)

    class Meta:
        model = CartItem
        fields = ['product', 'user', 'quantity']
