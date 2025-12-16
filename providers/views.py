from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import WorkingHours
from .serializers import WorkingHoursSerializer
from core.permissions import IsProvider, IsOwner
# Create your views here.

class WorkingHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated, IsProvider, IsOwner]
        if self.action == 'create':
            return [IsAuthenticated, IsProvider]
        return []
    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)
