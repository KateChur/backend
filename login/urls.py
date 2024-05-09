from django.urls import path
from rest_framework import routers
from . import views
from .views import UserViewSet
from django.conf.urls import include
from .views import login_view


router = routers.DefaultRouter()
router.register(r'login', UserViewSet)
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', include(router.urls)),
]
