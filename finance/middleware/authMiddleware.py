from django.http import JsonResponse
from django.conf import settings
import jwt  # PyJWT library for token decoding and validation

class AccessTokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define endpoints to exclude from token validation
        excluded_paths = ['/users/login/', '/users/signup/']
        if request.path in excluded_paths:
            return self.get_response(request)

        # Retrieve the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization token required'}, status=401)

        token = auth_header.split(' ')[1]  # Extract token

        try:
            # Validate the token using the SECRET_KEY from settings.py
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            
            # Optionally, attach user info to the request
            request.user_id = payload.get('user_id')  # Adjust field based on token payload structure
            
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Proceed to the next middleware or view if token is valid
        return self.get_response(request)
