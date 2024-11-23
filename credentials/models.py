from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing unique user ID
    email = models.EmailField(unique=True)  # Unique email field
    password = models.CharField(max_length=128)  # Password field (ideally hashed)
    created_on = models.DateTimeField()  # Automatically set on creation
    

    def check_password(self, raw_password):
        
        return check_password(raw_password, self.password)