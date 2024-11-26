from drf_spectacular.utils import OpenApiExample, extend_schema_serializer

from rest_framework import serializers

from .models import LocationData


class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = ["id", "device_id", "latitude", "longitude", "speed", "timestamp"]
        read_only_fields = ["timestamp"]

    @extend_schema_serializer(
        examples=[
            OpenApiExample(
                "Valid location data example",
                value={"device_id": "device123", "latitude": 41.0082, "longitude": 28.9784, "speed": 50.5},
                request_only=True,
            ),
        ]
    )
    def validate_latitude(self, value):
        """Latitude must be between -90 and 90 degrees"""
        try:
            float_value = float(value)
            if float_value < -90 or float_value > 90:
                raise serializers.ValidationError("Latitude must be between -90 and 90 degrees")
        except (TypeError, ValueError):
            raise serializers.ValidationError("Latitude must be a valid number")
        return value

    def validate_longitude(self, value):
        """Longitude must be between -180 and 180 degrees"""
        try:
            float_value = float(value)
            if float_value < -180 or float_value > 180:
                raise serializers.ValidationError("Longitude must be between -180 and 180 degrees")
        except (TypeError, ValueError):
            raise serializers.ValidationError("Longitude must be a valid number")
        return value

    def validate_speed(self, value):
        """Speed must be positive"""
        try:
            if float(value) < 0:
                raise serializers.ValidationError("Speed cannot be negative")
        except (TypeError, ValueError):
            raise serializers.ValidationError("Speed must be a valid number")
        return value

    def validate_device_id(self, value):
        """Device ID cannot be empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("Device ID cannot be empty")
        return value.strip()
