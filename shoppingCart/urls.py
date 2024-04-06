from django.urls import path
from .views import (get_cart,add_item , remove_item , update_quantity,get_total_price , change_cart_item_status)

urlpatterns = [
path ('',get_cart,name='cart'),
path ('add/', add_item , name='add_to_cart'),
path ('remove/<int:cart_item_id>/', remove_item , name='remove_from_cart'),
path ('update/<int:cart_item_id>/', update_quantity , name='update_quantity'),
path ('get_total_price/' ,get_total_price , name='get_total_price' ),
path ('cart_item/<int:cart_item_id>/', change_cart_item_status , name='change_cart_item_status' ),
]
