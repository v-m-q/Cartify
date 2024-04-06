from django.urls import path
from .views import get_orders,get_order_details

urlpatterns = [
    path('', get_orders, name='get_orders'),
    path('<int:order_id>/', get_order_details, name='get_order_detail'),
    # path('<int:order_id>/status', process_order, name='change_status'),
    # path('<int:order_id>/delete', delete_order, name='change_status'),
    # path('add/', new_order, name='change_status'),



]