from django.urls import path
from .views import (add_item , remove_item , update_quantity)



urlpatterns = [
    
path ('cart/add/', add_item , name='add_to_cart'),
path ('cart/remove/<int:cart_item_id>/', remove_item , name='remove_from_cart'),
path ('cart/update/<int:cart_item_id>/', update_quantity , name='update_quantity'),
]
