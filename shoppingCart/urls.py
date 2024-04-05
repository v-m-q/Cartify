from django.urls import path
from .views import (add_item , remove_item , update_quantity, get_cart)

urlpatterns = [
    path ('', get_cart, name='get_cart_details'),
    path ('add/', add_item , name='add_to_cart'),
    path ('remove/<int:cart_item_id>/', remove_item , name='remove_from_cart'),
    path ('update/<int:cart_item_id>/', update_quantity , name='update_quantity'),

]