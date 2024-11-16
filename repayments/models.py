from django.db import models
from customers.models import CustomerModel
from loans.models import LoanModel

class RepaymentModel(models.Model):
    repayment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)  # Link to CustomerModel
    loan_id = models.ForeignKey(LoanModel, on_delete=models.CASCADE)  # Link to LoanModel
    repayment_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount repaid
    payment_date = models.DateField()  # Date of repayment
    comments = models.TextField(blank=True, null=True)  # Optional comments field
