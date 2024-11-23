from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerModel
from datetime import datetime
import json
from django.http import JsonResponse
from users.models import AgentModel 


@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            
            # Retrieve the required fields from the JSON data
            agent_id = data.get('agent_id')
            customer_name = data.get('customer_name')
            customer_mobile_number = data.get('customer_mobile_number')
            alternate_mobile_number = data.get('alternate_mobile_number')
            date_of_birth = data.get('date_of_birth')
            aadhar_number = data.get('aadhar_number')
            pan_number = data.get('pan_number')
            address = data.get('address')

            # Retrieve the AgentModel object based on the agent_id
            agent = AgentModel.objects.get(agent_id = agent_id)

            # Create a new customer instance
            customer = CustomerModel.objects.create(
                agent_id=agent,
                customer_name=customer_name,
                customer_mobile_number=customer_mobile_number,
                alternate_mobile_number=alternate_mobile_number,
                date_of_birth=date_of_birth,
                aadhar_number=aadhar_number,
                pan_number=pan_number,
                address=address
            )

            # Save the customer instance to the database
            customer.save()

            # Return a success response
            return JsonResponse({'message': 'Customer added successfully'}, status=201)

        except AgentModel.DoesNotExist:
            return JsonResponse({'error1': 'Agent not found'}, status=404)
        except KeyError as e:
            return JsonResponse({'error2': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error3': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from customers.models import CustomerModel
from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def get(request, agent_id):
    try:
        # Filter customers based on agent_id
        customers = CustomerModel.objects.filter(agent_id=agent_id)
        
        # Check if any customers exist for the given agent_id
        if not customers.exists():
            return JsonResponse({'error': 'No customers found for the given agent_id'}, status=404)
        
        # Prepare data to return as a list of dictionaries
        customer_data = []
        for customer in customers:
            customer_data.append({
                'customer_id': customer.customer_id,
                'agent_id': customer.agent_id_id,
                'agent_name': customer.agent_id.name, 
                'customer_name': customer.customer_name,
                'customer_mobile_number': customer.customer_mobile_number,
                'alternate_mobile_number': customer.alternate_mobile_number,
                'date_of_birth': customer.date_of_birth,
                'aadhar_number': customer.aadhar_number,
                'pan_number': customer.pan_number,
                'address': customer.address,
            })
        
        # Return the data as JSON (set safe=False as we are returning a list)
        return JsonResponse(customer_data, safe=False, status=200)
    
    except Exception as e:
        # If any other exception occurs, return the exception message
        return JsonResponse({'error': str(e)}, status=500)




