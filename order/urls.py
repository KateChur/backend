from rest_framework import routers
from .views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
urlpatterns = router.urls
