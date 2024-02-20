from rest_framework import serializers

from laboratoire.models import Laboratoire


class LaboratoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratoire
        fields = '__all__'
