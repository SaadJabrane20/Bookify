from rest_framework import serializers
from .models import Booking
from providers.models import WorkingHours
from django.utils.timezone import make_aware
from datetime import datetime
from django.utils import timezone

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

    def validate(self, data):
        provider = data["provider"]
        start = data["start_time"]
        end = data["end_time"]
        if start >= end:
            raise serializers.ValidationError("End time must be after start time.")
        if start < timezone.now():
            raise serializers.ValidationError("You cannot book a time in the past.")
        if start.time() < working_hours.start_time or end.time() > working_hours.end_time:
            raise serializers.ValidationError("Booking time is outside provider working hours.")
        
        weekday = start.weekday()
        try:
            working_hours = WorkingHours.objects.get(provider=provider, day_of_week=weekday)
        except WorkingHours.DoesNotExist:
            raise serializers.ValidationError("Provider does not work on this day.")
        overlapping = Booking.objects.filter(
            provider=provider,
            start_time__lt=end,
            end_time__gt=start,
            status__in=["pending", "confirmed"],
        )
        if overlapping.exists():
            raise serializers.ValidationError(
                "This time slot is already booked for this provider."
            )
        return data
    
    def create(self, validated_data):
        user = self.context["request"].user

        validated_data["customer"] = user
        validated_data["status"] = "pending"

        return super().create(validated_data)
    