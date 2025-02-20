from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about_us/', views.AboutPageView.as_view(), name='about_us'),
]
