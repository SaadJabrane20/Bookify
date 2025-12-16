from django.shortcuts import render
from .serializers import BookingSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Booking
from core.permissions import IsClient
# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        user = self.request.user

        
        if user.profile.role == 'client':
            return Booking.objects.filter(customer=user)
        
        
        if user.profile.role == 'provider':
            return Booking.objects.filter(provider=user)
        
        return Booking.objects.none()
        
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(customer=user, status="pending")
    