"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shoppingCart.views import get_cart , add_item , remove_item , update_quantity , get_total_price
from . import views

urlpatterns = [
    path('', views.getHomeData),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path ('cart/', get_cart , name='shopping_cart'),
    path ('cart/add/', add_item , name='add_to_cart'),
    path ('cart/remove/', remove_item , name='remove_from_cart'),
    path ('/cart/<int:cartitem_id>/quantity/', update_quantity , name='update_quantity'),
    path ('/cart/total-price', get_total_price , name='get_total_price'),


]
