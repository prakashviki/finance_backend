from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AgentModel
from users.models import UserModel
from datetime import datetime
import json
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password


@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if UserModel.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        user = UserModel(
        email = data.get('email'),  
        password = make_password(data.get('password')),  
        created_on = datetime.now(),
        modified_on = datetime.now()
        )

        agent = AgentModel(
            finance_name=data.get('finance_name'),
            name=data.get('name'),
            dob=data.get('dob'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            address=data.get('address'),
            agent_type=data.get('agent_type'),
            created_on = datetime.now(),
            modified_on = datetime.now()
        )
       

        try:
        
            user.save() 
            agent.save()
            
            
            return JsonResponse({'message': 'Created successfully!'}, status=201)
        except Exception as e:
            
            return JsonResponse({'message': 'Something went wrong'}, status=500)

        

        




