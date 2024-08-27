from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'User already exists'}, status=400)
        
        user = User.objects.create(email=email, password=password)
        user.save()
        return JsonResponse({'message': 'Signup successful'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'message': 'Invalid password'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=400)


