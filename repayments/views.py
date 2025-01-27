from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import RepaymentModel, CustomerModel, LoanModel
import json

@csrf_exempt  # Disable CSRF token requirement for this example (not recommended for production)
def add(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Extract data from the JSON
            # customer_id = data.get('customer_id')
            loan_id = data.get('loan_id')
            repayment_amount = data.get('repayment_amount')
            payment_date = data.get('payment_date')
            comments = data.get('comments', '')

            # Get the customer and loan objects
            # customer = get_object_or_404(CustomerModel, pk=customer_id)
            loan = get_object_or_404(LoanModel, pk=loan_id)

            # Create a new repayment record
            repayment = RepaymentModel.objects.create(
                # customer_id=customer,
                loan_id=loan,
                repayment_amount=repayment_amount,
                payment_date=payment_date,
                comments=comments
            )

            # Return success response
            return JsonResponse({
                'status': 'success',
                'message': 'Repayment data saved successfully!',
                'repayment_id': repayment.repayment_id
            }, status=201)

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method. Only POST allowed.'
    }, status=405)
