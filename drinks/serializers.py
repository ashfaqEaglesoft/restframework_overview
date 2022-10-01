from dataclasses import field
from rest_framework import serializers
from .models import drinks

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=drinks
        fields='__all__'