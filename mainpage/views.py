from rest_framework import viewsets

from .models import Event_item
from .serializers import Event_itemSerializer


class Event_itemViewSet(viewsets.ModelViewSet):
    queryset = Event_item.objects.all()
    serializer_class = Event_itemSerializer

# Create your views here.
