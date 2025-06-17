from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Customise the appearance of the User model on admin page
    list_display = ("id", "username", "email", "first_name", "last_name", "date_joined") # Selects fields to show
    search_fields = ("username", "email") # Allows for searching with these fields
    list_filter = ("date_joined",) # Allows for filtering users
    ordering = ("-date_joined",) # Orders the users, newest first
