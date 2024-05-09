from django.contrib import admin
from eventpage.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_one',)
