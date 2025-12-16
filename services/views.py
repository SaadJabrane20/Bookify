from django.shortcuts import render
from .models import Service, ServiceCategory
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import ServiceSerializer, ServiceCategorySerializer
from core.permissions import IsProvider
# Create your views here.

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated, IsProvider]
        return []
    
    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)