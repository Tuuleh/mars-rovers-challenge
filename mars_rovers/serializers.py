from rest_framework import serializers
from mars_rovers.models import Plane, Rover


class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fields = ['id', 'direction', 'latitude', 'longitude']


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'width', 'height']
