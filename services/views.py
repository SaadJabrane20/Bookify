from django.shortcuts import render
from .models import Service, ServiceCategory
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ServiceSerializer, ServiceCategorySerializer

# Create your views here.

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)