from django.urls import path
from . import views

urlpatterns =[
    path('', views.getProductsByWishlist, name='wishlist'),
    path('add-to-wishlist/', views.addProductsToWishlist, name='add-to-wishlist'),
    path('remove-from-wishlist/', views.removeProductsToWishlist, name='remove-from-wishlist'),
]