from rest_framework import serializers
from .models import Region, Historical

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['geoName', 'miami_heat', 'boston_celtics']

class HistoricalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ['date', 'miami_heat', 'isPartial']