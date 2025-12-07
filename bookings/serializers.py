from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "customer",
            "provider",
            "service",
            "start_time",
            "end_time",
            "status",
        ]
        read_only_fields = ['customer', 'status']
    def create(self, validated_data):
        user = self.context["request"].user

        validated_data["customer"] = user
        validated_data["status"] = "pending"

        return super().create(validated_data)
    
    
        