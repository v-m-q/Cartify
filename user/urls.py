from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # account/
    path('', UserAPI.as_view()),
    
    # account/update
    path('update', UserAPI.as_view()),
    
    # account/login
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
]
