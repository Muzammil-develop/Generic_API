from rest_framework import serializers
from home.models import Car

class CarSerializer (serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'