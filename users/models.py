from django.db import models

# Create your models here.
class User(models.Model):
    # Id is created automatically
    username = models.CharField(max_length=256, unique=True) # Enforces unique username
    email = models.EmailField(unique=True) # Enforces unique email
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
