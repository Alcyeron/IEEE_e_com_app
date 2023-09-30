from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shop(request):
    return HttpResponse("<h1>Shop Home</h1>")
def products(request):
    return HttpResponse("<h1>Shop products</h1>")