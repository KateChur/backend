from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        print("hello")
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required.'}, status=400)

        hashed_password = make_password(password)

        try:
            user = User.objects.create(username=username, password=hashed_password)
            return JsonResponse({'message': 'User registered successfully.'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


# # работающий
# @csrf_exempt
# def register(request):
#     if request.method == 'GET':
#         user_form = RegistrationForm()
#     if request.method == 'POST':
#         user_form = RegistrationForm(request.POST)
#         print("hello")
#         if user_form.is_valid():
#             username = user_form.cleaned_data['username']
#             email = user_form.cleaned_data['email']
#             # password = user_form.cleaned_data['password']
#             password = request.POST.get('password')
#             hashed_password = make_password(password, hasher=PBKDF2PasswordHasher())
#             user = User.objects.create_user(username=username, email=email, password=hashed_password)
#             # user.set_password(password)
#             user.save()
#             user = user_form.save()
#             print(user)

# @api_view(['POST'])
# def register(request):
#     username = request.get('username')
#     password = request.get('password')
#
#     hashed_password = make_password(password)
#     print(hashed_password)
#
#     try:
#         user = User.objects.create(username=username, password=hashed_password)
#         return Response(status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




