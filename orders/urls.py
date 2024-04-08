from django.urls import path
from .views import create_order,add_item, get_orders,delete_order,delete_item,update_status
urlpatterns = [

    path('', get_orders, name='get-orders'),  
    path('create/', create_order, name='order-create'),
    path('<int:order_id>/add_item/', add_item, name='add-item'),
    path('<int:order_id>/delete_order/', delete_order, name='delete-order'),
    path('<int:order_id>/<int:item_id>/delete_item/', delete_item, name='delete-item'),
    path('<int:order_id>/update_status/', update_status, name='update_status'),
]
