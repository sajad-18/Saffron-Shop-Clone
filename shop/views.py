from django.shortcuts import render
from django.views import View


class ShopView(View):
    def get(self, request):
        return render(request, 'shop/shop.html')


class ProductsView(View):
    def get(self, request):
        return render(request, 'shop/products.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'shop/product-1.html')
