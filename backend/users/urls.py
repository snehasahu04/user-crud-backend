from django.urls import path

from .views import (
    UserProfileListCreateAPIView,
    UserProfileRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('users/', UserProfileListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
]
