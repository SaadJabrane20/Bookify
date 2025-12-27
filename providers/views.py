from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import WorkingHours
from .serializers import WorkingHoursSerializer
from core.permissions import (IsProvider,
                                IsOwner,
                                IsWorkingHoursOwner)
# Create your views here.

class WorkingHoursViewSet(viewsets.ModelViewSet):
    serializer_class = WorkingHoursSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.profile.role == "provider":
            return WorkingHours.objects.filter(provider=user)
        return WorkingHours.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated(), IsProvider()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsProvider(), IsWorkingHoursOwner()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

