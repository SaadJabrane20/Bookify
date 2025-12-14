from django.shortcuts import render
from .serializers import BookingSerializer
from rest_framework import viewsets, permissions
# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = 