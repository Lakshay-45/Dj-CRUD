from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Creating a router for url mapping
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

#  APIs will be managed automatically by the router
urlpatterns = [
    path('', include(router.urls))
]