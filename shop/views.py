from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, CreateView, View
from .models import Product, CartItem
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddToCartForm

# Create your views here.
items = [
    {
        'name': "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating': 4.2,
        'price': 2149,
        'mrp': 2199,
        'discount': 2
    },
    {
        'name': "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating': 4.3,
        'price': 1699,
        'mrp': 2499,
        'discount': 32
    },
    {
        'name': "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating': 4.3,
        'price': 1699,
        'mrp': 2499,
        'discount': 32
    },
    {
        'name': "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating': 4.2,
        'price': 2149,
        'mrp': 2199,
        'discount': 2
    },
    {
        'name': "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating': 4.3,
        'price': 1699,
        'mrp': 2499,
        'discount': 32
    },
    {
        'name': "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
        'rating': 4.2,
        'price': 2149,
        'mrp': 2199,
        'discount': 2
    },
    {
        'name': "MI 10000mAh Lithium Ion, Lithium Polymer Power Bank Pocket Pro with 22.5 Watt Fast Charging",
        'rating': 4.3,
        'price': 1699,
        'mrp': 2499,
        'discount': 32
    }
]


def shop(request):
    return render(request, "shop/shop.html")


def products(request):
    content_p = {
        'title': "Products",
        'products': Product.objects.all()
    }
    return render(request, "shop/products.html", content_p)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_values = {
            'user': self.request.user,
            'product': self.get_object()
        }
        context["form"] = AddToCartForm(initial=form_values)
        return context


class AddToCartView(LoginRequiredMixin, CreateView):
    template_name = "shop/product_detail.html"
    form_class = AddToCartForm
    model = CartItem
    success_url = '/cart'

    def form_valid(self, form):
        return super().form_valid(form)


@login_required
def view_cart(request):
    content_c = {
        'title': "Cart",
        'items': request.user.cartitem_set.all()
    }
    return render(request, "shop/cartitem_list.html", content_c)


class CartView(View):
    def get(self, request, *args, **kwargs):
        return view_cart(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AddToCartView.as_view()
        return view(request, *args, **kwargs)


def orders(request):
    content_o = {
        'title': "Orders"
    }
    return render(request, "shop/orders.html", content_o)
