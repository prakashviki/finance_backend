from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UsersModel
from datetime import datetime
import json
from django.http import JsonResponse
# from django.contrib.auth.hashers import make_password, check_password
from . import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.serializers import serialize
import random
from django.utils import timezone



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        def generate_unique_admin_id():
            while True:
                admin_id = random.randint(10000, 99999)  # Generate a random 5-digit number
                if not UsersModel.objects.filter(admin_id=admin_id).exists():  # Ensure it's unique
                    return admin_id
        
        admin_id=data.get('admin_id') or generate_unique_admin_id()
        password = data.get('password')

       

        if UsersModel.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        if data['role'] == 'agent':
            if not UsersModel.objects.filter(admin_id = data['admin_id']  ).exists():
                return JsonResponse({'error':'Invalid Admin ID'}, status=401)

            if not UsersModel.objects.filter(mobile_number = data['admin_mobile_number'] ).exists() :
                return JsonResponse({'error':'Invalid Admin Mobile Number'}, status=401)

    user = UsersModel(
    role= data.get('role'),
    mobile_number=data.get('mobile_number'),
       # Hash the password before saving
    
    admin_id=admin_id, 
    
    email=data.get('email'),
    finance_name=data.get('finance_name'),
    user_name=data.get('user_name'),
    created_on= timezone.now()
    )
    password=user.set_password(password)
    try:
        user.save() 
        return JsonResponse({'message': 'Created successfully!'}, status=201)
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Something went wrong'}, status=500)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            # Parse the request body for email and password
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data format'}, status=400)

        # Try to retrieve the user by email
        try:
            user = UsersModel.objects.get(email=email)
        except UsersModel.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

        # Check the user's password
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            user_data = json.loads(serialize('json', [user]))[0]['fields']
            if 'password' in user_data:
                del user_data['password']
            refresh.payload['user'] = user_data 

            access_token = str(refresh.access_token)        
            # Return success response with user ID
            return JsonResponse({
                    'user_id':user.user_id,
                    'admin_id':user.admin_id,
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': access_token,
                }, status=200)
            # return JsonResponse({'message': 'Login successful', 'user_id': user.user_id}, status=200)
        else:
            # Invalid credentials
            print("Failed at this level")
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

    # If the request method is not POST
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)




