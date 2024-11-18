from django.contrib.auth import authenticate, login as django_login
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from .models import UserModel
import json
from django.core.serializers import serialize

@csrf_exempt  # Optional: You may want to keep CSRF protection enabled in production
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
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
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

from django.contrib.auth import logout as django_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        django_logout(request)  # This will clear the session and log the user out
        return JsonResponse({'message': 'Logout successful!'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)