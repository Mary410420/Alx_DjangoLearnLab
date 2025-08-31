from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', feed, name='feed'),
    path('', include(router.urls)),  # /posts/, /comments/, plus /posts/<pk>/like/ and /unlike/
]
