from rest_framework import serializers

from agriculteur.models import Agriculteur


class AgriculteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agriculteur
        fields = '__all__'
