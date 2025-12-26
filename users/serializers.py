from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from djoser.serializers import UserCreateSerializer

class CustomUserCreateSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        write_only=True
    )

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ("role",)

    def validate(self, attrs):
        # Extract role BEFORE Djoser creates the User
        self.role = attrs.pop("role", None)
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)

        # Assign role after user + profile exist
        if self.role:
            user.profile.role = self.role
            user.profile.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role")

    class Meta:
        model = User
        fields = ("id", "username", "email", "role")
