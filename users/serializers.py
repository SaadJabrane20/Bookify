from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(
        choices=Profile.User_roles,
        write_only=True
    )

    class Meta:
        model = User
        fields = ("id", "username", "password", "role")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = User.objects.create_user(**validated_data)
        user.profile.role = role
        user.profile.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role")

    class Meta:
        model = User
        fields = ("id", "username", "email", "role")
