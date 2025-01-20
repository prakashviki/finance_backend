from django.contrib import admin
from .models import CustomerModel
@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('agent_id','customer_id', 'customer_name', 'customer_mobile_number','alternate_mobile_number', 'date_of_birth', 'aadhar_number', 'pan_number')
    search_fields = ('customer_name', 'aadhar_number', 'pan_number')
    list_filter = ('date_of_birth',)

# # Register the model and the admin class
# admin.site.register(CustomerModel, CustomerModelAdmin)
