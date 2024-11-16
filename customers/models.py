from django.db import models
from agents.models import AgentModel

class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    agent_id =  models.ForeignKey(AgentModel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_mobile_number = models.CharField(max_length=15)
    alternate_mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    pan_number = models.CharField(max_length=10, unique=True)

    #  Photo fields for the customer and their Aadhar image
    # photo = models.ImageField(upload_to='customer_photos/', blank=True, null=True)
    # aadhar_image = models.ImageField(upload_to='aadhar_images/', blank=True, null=True)
    address = models.TextField()

