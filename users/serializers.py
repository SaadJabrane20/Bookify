from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'role',
            'phone_number',
            'category',
            ]
        read_only_fields = ["user"]