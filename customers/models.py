from django.db import models
from users.models import UsersModel
import uuid

class CustomerModel(models.Model):
    customer_id = customer_id = models.AutoField(primary_key=True)
    user_id =  models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_mobile_number = models.CharField(max_length=15)
    alternate_mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    aadhar_number = models.CharField(max_length=15, unique=True)
    pan_number = models.CharField(max_length=10, unique=True)
    address = models.TextField()

    #  Photo fields for the customer and their Aadhar image
    # photo = models.ImageField(upload_to='customer_photos/', blank=True, null=True)
    # aadhar_image = models.ImageField(upload_to='aadhar_images/', blank=True, null=True)

