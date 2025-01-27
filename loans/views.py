import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import LoanModel
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from .models import LoanModel
from repayments.models import RepaymentModel  # Assuming you have a Repayment model
from customers.models import CustomerModel
import traceback

import json
from customers.models import CustomerModel
from django.shortcuts import get_object_or_404

@csrf_exempt  # Use this for simplicity; in production, use proper CSRF handling
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract the data from the request
            customer_id = data.get('customer_id')
            customer_instance = get_object_or_404(CustomerModel, customer_id=customer_id)

            loan_amount = data.get('loan_amount')
            repayment_amount = data.get('repayment_amount')
            repayment_frequency = data.get('repayment_frequency')
            
            number_of_installments = data.get('number_of_installments')
            lending_date = data.get('lending_date')

            agent = CustomerModel.objects.get(customer_id = customer_id)

            # Create a new loan instance
            loan = LoanModel(
                customer_id=customer_instance,
                loan_amount=loan_amount,
                repayment_amount=repayment_amount,
                repayment_frequency=repayment_frequency,
                number_of_installments=number_of_installments,
                lending_date = lending_date
            )

            # Save the loan instance to the database
            loan.save()

            return JsonResponse({'message': 'Loan created successfully', 'loan_id': loan.loan_id}, status=201)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=400)
        except CustomerModel.DoesNotExist:
            traceback.print_exc()
            return JsonResponse({'error1': 'Customer not found'}, status=404)
    traceback.print_exc()
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt
def loan_details(request, loan_id):
    try:
        # Fetch the loan details by loan_id
        loan = get_object_or_404(LoanModel, loan_id=loan_id)

        

        # Fetch all repayments associated with the loan
        repayments = RepaymentModel.objects.filter(loan_id=loan)  # Assuming RepaymentModel has a ForeignKey to LoanModel

        # Prepare the repayment details to be returned in the response
        repayment_details = []
        for repayment in repayments:
            repayment_details.append({
                'repayment_id': repayment.repayment_id,
                'repayment_amount': repayment.repayment_amount,
                'repayment_date': repayment.payment_date,
                'comments': repayment.comments
            })

        # Prepare the loan details to be returned
        loan_details = {
            'loan_id': loan.loan_id,
            'loan_amount': loan.loan_amount,
            'repayment_amount': loan.repayment_amount,
            'repayment_frequency': loan.repayment_frequency,
            'number_of_installments': loan.number_of_installments,
            'lending_date': loan.lending_date,
            'no_of_repayments_paid':len(repayment_details),
            
            'repayments': repayment_details
        }

        return JsonResponse(loan_details, status=200)

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=400)

