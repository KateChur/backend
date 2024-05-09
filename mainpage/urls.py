from rest_framework import routers

from .views import Event_itemViewSet

router = routers.DefaultRouter()
router.register(r'mainpage', Event_itemViewSet)

urlpatterns = router.urls
