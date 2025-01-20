# admin.py

from django.contrib import admin
from .models import LoanModel

class LoanModelAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'customer_id', 'loan_amount',  'repayment_amount', 
                    'repayment_frequency', 'number_of_installments', 
                    'lending_date')
    search_fields = ('customer__customer_name', 'loan_amount')
    list_filter = ('repayment_frequency', 'lending_date')

admin.site.register(LoanModel, LoanModelAdmin)
