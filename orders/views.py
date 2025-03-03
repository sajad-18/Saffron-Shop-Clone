from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from shop.models import Products
from .forms import CartAddForm
from .cart import CART


class CartView(View):
    def get(self, request):
        cart = CART(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = CART(request)
        product = get_object_or_404(Products, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = CART(request)
        product = get_object_or_404(Products, id=product_id)
        cart.remove(product)
        return redirect('orders:cart')
