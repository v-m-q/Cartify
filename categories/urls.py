from django.urls import path
from . import views

urlpatterns = [
    path('', views.Categories, name='categories')
]