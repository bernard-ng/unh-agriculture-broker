from rest_framework import serializers

from transporteur.models import Transporteur


class TransporteurInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporteur
        fields = '__all__'
