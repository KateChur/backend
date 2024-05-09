from typing import Any

from pyexpat.errors import messages
from rest_framework import viewsets
from django.contrib.auth.models import User
from .forms import LoginForm
from .serializers import UserSerializer
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @csrf_exempt
# def login_view(request):
#     if request.method == 'GET':
#         user_form = LoginForm()
#     if request.method == 'POST':
#         user_form = LoginForm(request.POST)
#         if user_form.is_valid():
#             username = user_form.cleaned_data['username']
#             password = user_form.cleaned_data['password']
#             user = authenticate(request=request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({'success': True})
#     return JsonResponse({'success': False})


# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request=request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('http://localhost:5173/')
#         else:
#             return JsonResponse({'success': False, 'error': 'Wrong username or password'}, status=400)
#     else:
#         return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)

# УДАЧНЫЙ С ВОЗВРАТОМ TRUE FALSE
# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request=request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({'success': True})
#     return JsonResponse({'success': False})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        print(request.POST)
        # user = authenticate(request=request, username=username, password=password)
        user = authenticate(request=request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('Logged in successfully!')
            # ВЕРНЫЙ

            # response.set_cookie('isLoggedIn', 'True')
            # return response
            print(user.first_name, user.last_name)
            print(user.first_name, user.last_name)
            return JsonResponse({'first_name': user.first_name, 'last_name': user.last_name, 'code': 200, 'isLoggedIn': True})
    return JsonResponse({'code': 400, 'message': 'Invalid username or password'})

