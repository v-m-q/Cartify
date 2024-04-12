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
    # account/signup
    path('signup', RegisterView.as_view(), name='auth_register'),
    
    # account/signin
    path('signin', LoginView.as_view(), name='token_obtain_pair'),
    
    # account/
    path('', UserAPI.as_view()),
    
    # account/update
    path('update', UserAPI.as_view()),
    
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]
