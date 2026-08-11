from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from .views import (
    CurrentUserAPIView,
    CustomTokenRefreshAPIView,
    EmailTokenObtainPairAPIView,
    RegisterAPIView,
    UserProfileListCreateAPIView,
    UserProfileRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/login/', EmailTokenObtainPairAPIView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', CustomTokenRefreshAPIView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/me/', CurrentUserAPIView.as_view(), name='current_user'),
    path('users/', UserProfileListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
]
