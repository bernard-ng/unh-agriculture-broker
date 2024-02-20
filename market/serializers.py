from rest_framework import serializers

from market.models import Market


class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'
