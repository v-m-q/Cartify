from django.urls import path
from .views import (LoginView,RegisterView)
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    #Authentication
    path('signin', LoginView.as_view(), name='token_obtain_pair'),
    path('signup', RegisterView.as_view(), name='auth_register'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # account/
    path('', UserAPI.as_view()),
    
    # account/update
    path('update', UserAPI.as_view()),
    
    # account/login
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
]
