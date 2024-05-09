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



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()


@csrf_exempt
def register(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        print("hello")
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            # password = user_form.cleaned_data['password']
            password = request.POST.get('password')
            hashed_password = make_password(password, hasher=PBKDF2PasswordHasher())
            user = User.objects.create_user(username=username, email=email, password=hashed_password)
            # user.set_password(password)
            user.save()
            user = user_form.save()
            print(user)



