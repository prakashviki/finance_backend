from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'password','created_on', 'modified_on')  # Specify fields to display
    search_fields = ('email',)  # Optional: add search functionality
