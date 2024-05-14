from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Получаем пользователя из базы данных по имени пользователя
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Если пользователя не существует, возвращаем сообщение об ошибке
            return JsonResponse({'code': 400, 'message': 'Invalid username or password'})

        # Проверяем, совпадает ли введенный пароль с паролем пользователя из базы данных
        if user.password == password:
            # Если пароли совпадают, выполняем вход
            login(request, user)
            print('Logged in successfully!')
            return JsonResponse(
                {'first_name': user.first_name, 'last_name': user.last_name, 'code': 200, 'isLoggedIn': True})
        else:
            # Если пароли не совпадают, возвращаем сообщение об ошибке
            return JsonResponse({'code': 400, 'message': 'Invalid username or password'})

    return JsonResponse({'code': 400, 'message': 'Invalid request method'})