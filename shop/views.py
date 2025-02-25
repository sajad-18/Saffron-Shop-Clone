from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Products, Category


class ShopView(View):
    def get(self, request):
        return render(request, 'shop/shop.html')


class ProductsView(View):
    def get(self, request, category_slug=None):
        products = Products.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        sort_option = request.GET.get('sort', 'default')
        if sort_option == "low-to-high":
            products = products.order_by('-price')
        elif sort_option == "high-to-low":
            products = products.order_by('price')
        elif sort_option == "newest":
            products = products.order_by('created')

        return render(request, 'shop/products.html', {'products': products, 'categories': categories})


class ProductsDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        return render(request, 'shop/detail.html', {'product': product})


class ShowProductView(View):
    def get(self, request):
        products = Products.objects.filter(available=True)
        return render(request, 'inc/shop-navbar.html', {'products': products})
