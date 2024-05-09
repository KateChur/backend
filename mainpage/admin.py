from django.contrib import admin

from mainpage.models import Event_item, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Event_item)
class Event_itemAdmin(admin.ModelAdmin):
    model = Event_item

    list_display = ('title', 'price')
