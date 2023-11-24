from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Wallet


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    amount = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("database not committed")
        user = super().save()
        balance = Wallet.objects.create(user=user, balance=self.cleaned_data.get('amount'))
        return user, balance


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AmountAddForm(forms.Form):
    amount = forms.IntegerField()

