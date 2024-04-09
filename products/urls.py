from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts , name='products'),
    path('<int:ProductId>/', views.GetProduct),
    path('category/<int:CategoryId>/', views.getProductsByCategory, name='productsByCategory'),
    path('search/', views.ProductListView.as_view(), name='search'),
]
