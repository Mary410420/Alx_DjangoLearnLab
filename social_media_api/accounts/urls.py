from django.urls import path
from .views import RegisterView, LoginView, ProfileView, feed

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('feed/', feed, name='feed'),
    
]
