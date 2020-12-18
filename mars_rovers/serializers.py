from rest_framework import serializers
from mars_rovers.models import Plane, Rover


class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fields = ['id', 'direction', 'owner', 'plane_id', 'latitude', 'longitude']


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'width', 'height']


# class RoverSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direction = serializers.CharField(required=True, allow_blank=False, max_length=1)
#     owner = serializers.ReadOnlyField(source='owner.username')
#     plane_id = serializers.IntegerField(read_only=True)
#     latitude = serializers.IntegerField()
#     longitude = serializers.IntegerField()

# def create(self, validated_data):
#     return Rover.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.direction = validated_data.get('direction', instance.direction)
#     instance.latitude = validated_data.get('latitude', instance.latitude)
#     instance.longitude = validated_data.get('longitude', instance.longitude)
#     instance.save()
#     return instance


class PlaneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    width = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(read_only=True)
