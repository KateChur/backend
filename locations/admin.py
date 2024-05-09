from django.contrib import admin
from locations.models import Locations


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    model = Locations
    list_display = ('name', 'description')
