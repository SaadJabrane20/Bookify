from rest_framework import serializers
from .models import ServiceCategory, Service

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "provider",
            "category",
            "name",
            "description",
            "duration",
            "price",
        ]
        read_only_fields = ["provider"]

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be positive.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value
    