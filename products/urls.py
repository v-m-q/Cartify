from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts),
    path('<int:product_id>/', views.GetProduct),
    path('category/<int:category_id>/', views.getProductsByCategory, name='productsByCategory'),
    path('search/', views.ProductListView.as_view(), name='search'),
]
