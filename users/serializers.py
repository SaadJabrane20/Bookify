from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from djoser.serializers import UserCreateSerializer

class CustomUserCreateSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(
        choices=Profile.ROLE_CHOICES, write_only=True
    )
    class Meta(UserCreateSerializer.Meta):
        fields = ("id", "username", "password", "email", "role")

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = super().create(validated_data)
        user.profile.role = role
        user.profile.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role")

    class Meta:
        model = User
        fields = ("id", "username", "email", "role")
