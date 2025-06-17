from rest_framework import serializers
from .models import User

# Used for serializing the data into json objects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "date_joined"]
        read_only_fields = ["date_joined"]