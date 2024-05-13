from rest_framework import routers
from .views import RecommendationViewSet
from django.urls import path
from . import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'recommendations', RecommendationViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('recommendations/', views.search_documents, name='recommendations'),
]
