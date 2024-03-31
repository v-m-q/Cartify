from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('<int:ProductId>/', views.GetProduct),
    path('search/', views.ProductListView.as_view(), name='search'),
]
