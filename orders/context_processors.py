from .cart import CART
from shop.models import Products

def cart(request):
    return {'cart': CART(request)}

def products(request):
    return {'products': Products.objects.all()}
