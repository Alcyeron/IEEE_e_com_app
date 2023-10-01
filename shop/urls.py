from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name = "shop-home"),
    path('products/', views.products, name = "shop-products"),
    path('wallet/', views.wallet, name = "shop-wallet"),
    path('orders/', views.orders, name = "shop-orders"),
]
