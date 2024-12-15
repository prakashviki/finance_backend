from django.contrib import admin
from .models import UsersModel

class UsersModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'role', 'mobile_number','admin_id', 'email', 'finance_name', 'user_name','password', 'created_on')
    search_fields = ('user_name', 'email', 'mobile_number')  # Optional: Allows searching by these fields

admin.site.register(UsersModel, UsersModelAdmin)
