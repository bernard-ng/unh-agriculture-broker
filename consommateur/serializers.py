from rest_framework import serializers

from consommateur.models import Consommateur


class ConsommateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommateur
        fields = '__all__'
