from rest_framework import routers
from .views import UserViewSet
from django.urls import path
from . import views
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'register', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_view, name='register'),
]
