from rest_framework import routers

from .views import EventViewSet

router = routers.DefaultRouter()
router.register(r'eventpage', EventViewSet)

urlpatterns = router.urls
