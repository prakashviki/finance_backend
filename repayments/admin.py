from django.contrib import admin
from .models import RepaymentModel  # Assuming the model is called RepaymentModel

# Customizing the Repayment model's admin interface
class RepaymentModelAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('loan_id','repayment_id',  'repayment_amount', 'payment_date', 'comments')


    # Adding search functionality in the admin for repayment_amount and status
    search_fields = ('repayment_amount', 'status')

    # Allowing the admin to edit repayments in bulk
    actions = ['mark_as_paid', 'mark_as_pending']


# Registering the model with the customized admin interface
admin.site.register(RepaymentModel, RepaymentModelAdmin)
