from django.db import models
from customers.models import CustomerModel 
class LoanModel(models.Model):
    loan_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)  # Link to CustomerModel
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits as needed
    # roi = models.DecimalField(max_digits=5, decimal_places=2)  # Rate of Interest
    repayment_amount = models.IntegerField()
    repayment_frequency = models.CharField(max_length=20)  # e.g., monthly, quarterly
    
    number_of_installments = models.IntegerField()  # Number of installments for the loan
    lending_date = models.DateTimeField()

