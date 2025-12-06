from rest_framework import serializers
from .models import WorkingHours

class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields =  [
            "provider",
            "day_of_week",
            "start_time",
            "end_time",
        ]

        read_only_fields = ["provider"]