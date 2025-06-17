from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # Viewset for viewing and editing users
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer