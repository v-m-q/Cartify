from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', StudentAPI.as_view()),
    path('update', StudentAPI.as_view()),
    
    
    # path('login', views.Login.as_view(), name='login'),
    # path('signup/', views.signup),
    # path('update/', views.updateAccountData),
]
