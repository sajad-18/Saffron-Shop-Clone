from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Products


class ShopView(View):
    def get(self, request):
        return render(request, 'shop/shop.html')


class ProductsView(View):
    def get(self, request):
        products = Products.objects.filter(available=True)
        return render(request, 'shop/products.html', {'products': products})


class ProductView(View):
    def get(self, request):
        return render(request, 'shop/product-1.html')


class ProductsDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        return render(request, 'shop/detail.html', {'product': product})


class ShowProductView(View):
    def get(self, request):
        products = Products.objects.filter(available=True)
        return render(request, 'inc/shop-navbar.html', {'products': products})
