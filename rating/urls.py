from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/add-rating/', views.rate_product, name='add-rating'),
]