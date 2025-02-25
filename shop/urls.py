from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('category/<slug:category_slug>/', views.ProductsView.as_view(), name='category-filter'),
    path('<slug:slug>/', views.ProductsDetailView.as_view(), name='product_detail'),
]
