from django.urls import path
from . import views

urlpatterns = [
    path('<int:ProductId>/', views.productImages, name='images')
]