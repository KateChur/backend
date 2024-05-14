from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class RecommendationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recommendation
#         fields = '__all__'