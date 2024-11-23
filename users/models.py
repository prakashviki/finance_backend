from django.db import models


class AgentModel(models.Model):
    
    agent_id = models.AutoField(primary_key=True)
    finance_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    agent_type = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=10)
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()

    def __str__(self):
        return (
            f"Agent ID: {self.agent_id}, "
            f"Finance Name: {self.finance_name}, "
            f"Name: {self.name}, "
            f"DOB: {self.dob}, "
            f"Mobile Number: {self.mobile_number}, "
            f"Email: {self.email}, "
            f"Address: {self.address}, "
            f"Agent Type: {self.agent_type}, "
            f"Created On: {self.created_on}, "
            f"Modified On: {self.modified_on}"
        )

  
 