from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shop(request):
    return render(request, "shop/shop.html")
def products(request):
    return render(request, "shop/products.html")