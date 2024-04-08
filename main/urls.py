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
from django.conf.urls.static import static 
from . import views
from pathlib import Path
import os

from. import views

urlpatterns = [
    path('', views.getHomeData),
    path('pay/', include('payment.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('user.urls')),
    path('products/', include('products.urls')),
    path('images/', include('images.urls')),
    path('categories/', include('categories.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('cart/',include('shoppingCart.urls')),
    path('orders/',include ('orders.urls'))
]

BASE_DIR = Path(__file__).resolve().parent.parent
urlpatterns += static('media/', document_root=os.path.join(BASE_DIR, 'media'))
