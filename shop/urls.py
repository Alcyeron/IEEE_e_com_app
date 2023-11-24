from django.urls import path
from . import views

app_name = "shop_app"
urlpatterns = [
    path('', views.shop, name="shop-home"),
    path('products/', views.products, name="shop-products"),
    path('orders/', views.orders, name="shop-orders"),
]
