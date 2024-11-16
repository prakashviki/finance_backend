from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import LoanModel
from django.contrib.auth.decorators import login_required

import json
from customers.models import CustomerModel

@login_required
@csrf_exempt  # Use this for simplicity; in production, use proper CSRF handling
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract the data from the request
            customer_id = data.get('customer_id')
            loan_amount = data.get('loan_amount')
            roi = data.get('roi')
            emi_amount = data.get("emi_amount")
            repayment_frequency = data.get('repayment_frequency')
            
            number_of_installments = data.get('number_of_installments')
            lending_date = data.get('lending_date')

            agent = CustomerModel.objects.get(customer_id = customer_id)

            # Create a new loan instance
            loan = LoanModel(
                customer_id=customer_id,
                loan_amount=loan_amount,
                roi=roi,
                emi_amount = emi_amount,
                repayment_frequency=repayment_frequency,
               
                number_of_installments=number_of_installments,
                lending_date = lending_date
            )

            # Save the loan instance to the database
            loan.save()

            return JsonResponse({'message': 'Loan created successfully', 'loan_id': loan.loan_id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        except CustomerModel.DoesNotExist:
            return JsonResponse({'error1': 'Customer not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
