from django.urls import path
from . import views

urlpatterns =[
    path('', views.getProductsByWishlist, name='wishlist'),
    path('add/', views.addProductsToWishlist, name='addTOWishlist'),
    path('remove/', views.removeProductsToWishlist, name='removeFromWishlist'),
]