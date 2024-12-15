from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class UsersModel(models.Model):
    
    
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing unique user ID
    role = models.CharField( max_length=15)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Password field (ideally hashed)
    
    admin_id = models.CharField(max_length=10)
    
    email = models.EmailField(unique=True)  # Unique email field
    finance_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    created_on = models.DateTimeField()  

    def set_password(self, raw_password):
        # Hash the password using Django's method
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Check if the provided password matches the hashed password
        return check_password(raw_password, self.password)
    