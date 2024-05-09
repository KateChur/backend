from rest_framework import viewsets
from .models import Locations
from .serializers import LocationsSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    