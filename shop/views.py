from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
items = [
    {
        'name' : "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating' : 4.2,
        'price' : 2149,
        'mrp' : 2199,
        'discount' : 2
    },
    {
        'name' : "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating' : 4.3,
        'price' : 1699,
        'mrp' : 2499,
        'discount' : 32
    },
    {
        'name' : "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating' : 4.3,
        'price' : 1699,
        'mrp' : 2499,
        'discount' : 32
    },
    {
        'name' : "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating' : 4.2,
        'price' : 2149,
        'mrp' : 2199,
        'discount' : 2
    },
    {
        'name' : "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating' : 4.3,
        'price' : 1699,
        'mrp' : 2499,
        'discount' : 32
    },
    {
        'name' : "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating' : 4.2,
        'price' : 2149,
        'mrp' : 2199,
        'discount' : 2
    },
    {
        'name' : "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating' : 4.3,
        'price' : 1699,
        'mrp' : 2499,
        'discount' : 32
    }
]
def shop(request):
    return render(request, "shop/shop.html")
def products(request):
    content_p = {
        'title': "Products",
        'items' : items,
        'i' : 0
    }
    return render(request, "shop/products.html", content_p)
def wallet(request):
    content_w = {
        'title' : "Wallet"
    }
    return render(request, "shop/wallet.html", content_w)
def orders(request):
    content_o = {
        'title' : "Orders"
    }
    return render(request, "shop/orders.html", content_o)
