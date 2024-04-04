from django.urls import path
from .views import (LoginView,RegisterView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    #Authentication
    path('signin', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', RegisterView.as_view(), name='auth_register'),
]
