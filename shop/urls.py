from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/1/', views.ProductView.as_view(), name='product'),
    path('<slug:slug>/', views.ProductsDetailView.as_view(), name='product_detail')
]
