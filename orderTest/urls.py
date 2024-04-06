from django.urls import path
from .views import (order_detail,update_order_status ,order_list )

urlpatterns = [
 path ('',order_list,name='get_orders'),
 path ('<int:order_id>',order_detail,name='order_details'),
 path ('<int:order_id>/update_order_status',update_order_status,name='update_order_status'),
]
