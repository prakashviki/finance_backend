from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerModel
from datetime import datetime
import json
from django.http import JsonResponse
from users.models import UsersModel 
from django.core.exceptions import ObjectDoesNotExist
import traceback


from django.db import connection
@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            
            data = json.loads(request.body)
            
            user_id = int(data.get('user_id'))
            
           
            customer_name = data.get('customer_name')
           
            customer_mobile_number = data.get('customer_mobile_number')
            alternate_mobile_number = data.get('alternate_mobile_number')
            date_of_birth = data.get('date_of_birth')
            aadhar_number = data.get('aadhar_number')
            pan_number = data.get('pan_number')
            address = data.get('address')
            
            try:
                
                user = UsersModel.objects.get(user_id = user_id)
                print(user)

            except e as exception:
                return JsonResponse({'error': 'User not found'}, status=404)
            # Create a new customer instance
            customer = CustomerModel.objects.create(
                user_id=user,
                customer_name=customer_name,
                customer_mobile_number=customer_mobile_number,
                alternate_mobile_number=alternate_mobile_number,
                date_of_birth=date_of_birth,
                aadhar_number=aadhar_number,
                pan_number=pan_number,
                address=address
            )
            print("Test3")
            # Save the customer instance to the database
            customer.save()

            # Return a success response
            return JsonResponse({'message': 'Customer added successfully'}, status=201)

        except UsersModel.DoesNotExist:
            return JsonResponse({'error1': 'Agent not found'}, status=404)
        except KeyError as e:
            return JsonResponse({'error2': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error3': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from customers.models import CustomerModel
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get(request, agent_id):
    try:
        
        # Filter customers based on agent_id
        customers = CustomerModel.objects.filter(user_id=agent_id)
        # loans = 
        # Check if any customers exist for the given agent_id
        if not customers.exists():
            return JsonResponse({'error': 'No customers found for the given agent_id'}, status=404)
        
        # Prepare data to return as a list of dictionaries
        customer_data = []
        for customer in customers:
            customer_data.append({
                'customer_id': customer.customer_id,
                # 'agent_id': customer.user_id.user_id,
                # 'agent_name': customer.agent_id_name, 
                'customer_name': customer.customer_name,
                'customer_mobile_number': customer.customer_mobile_number,
                'pending_loan' : is_pending_loan(customer.customer_id),
                # 'alternate_mobile_number': customer.alternate_mobile_number,
                # 'date_of_birth': customer.date_of_birth,
                # 'aadhar_number': customer.aadhar_number,
                # 'pan_number': customer.pan_number,
                # 'address': customer.address,
            })
        
        # Return the data as JSON (set safe=False as we are returning a list)
        return JsonResponse(customer_data, safe=False, status=200)
    
    except Exception as e:
        # If any other exception occurs, return the exception message
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)

from loans.models import LoanModel
from repayments.models import RepaymentModel

def is_pending_loan( customer_id):
    
    loans = LoanModel.objects.filter(customer_id=customer_id)
    if loans:
        for loan in loans :
            loan_id = loan.loan_id
            repayments = RepaymentModel.objects.filter(loan_id = loan_id)
            count = repayments.count()
            
            if count < loan.number_of_installments:
                return True
            else:
                return False
    else:
        return False


@csrf_exempt
def get_customer_info(request, customer_id):
    try:
        # Fetch customer and related loans in one query
        customer = CustomerModel.objects.prefetch_related('loanmodel_set').get(customer_id=customer_id)

        loan_data = [
            {
                'loan_id': loan.loan_id,
                'loan_amount': loan.loan_amount,
                'pending_loan' : is_selected_loan_pending(loan.loan_id),

                
            }
            for loan in customer.loanmodel_set.all()
        ]

        # Prepare customer data
        customer_data = {
            'customer_id': customer.customer_id,
            'customer_name': customer.customer_name,
            'customer_mobile_number': customer.customer_mobile_number,
            'alternate_mobile_number': customer.alternate_mobile_number,
            
            'aadhar_number': customer.aadhar_number,
            'pan_number': customer.pan_number,
            'address': customer.address,
            'loans': loan_data,  # Include loan details in the response
        }

        return JsonResponse(customer_data, safe=False)

    except CustomerModel.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def is_selected_loan_pending(loan_id):
    loan = LoanModel.objects.get(loan_id=loan_id)
    repayments = RepaymentModel.objects.filter(loan_id=loan_id)
    count = repayments.count()
    if count < loan.number_of_installments:
        return True
    else:
        return False
