from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, AmountAddForm
from .models import Wallet
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('/profile/')
    else:
        u_form = UserUpdateForm(instance=request.user)
    content = {
        'u_form': u_form
    }
    return render(request, 'user/profile.html', content)


@login_required
def add_amount(request):
    if request.method == 'POST':
        w_form = AmountAddForm(request.POST)
        if w_form.is_valid():
            amount = w_form.cleaned_data.get('amount')
            wallet = User.objects.filter(username=request.user).first().wallet
            wallet.balance += amount
            wallet.save()
            messages.success(request, f"₹{amount} has been added to your account")
            return redirect('/wallet/')
    else:
        w_form = AmountAddForm()
    content_w = {
        'title': "Wallet",
        'w_form': w_form
    }
    return render(request, "user/wallet.html", content_w)
