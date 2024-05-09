from rest_framework import serializers

from .models import Event_item

class Event_itemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event_item
        fields = '__all__'
