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

        