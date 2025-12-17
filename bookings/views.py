from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Booking
from .serializers import BookingSerializer
from core.permissions import (
    IsClient,
    IsBookingCustomer,
    IsBookingProvider,
    IsCustomerOrProvider,
)

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.profile.role == "client":
            return Booking.objects.filter(customer=user)

        if user.profile.role == "provider":
            return Booking.objects.filter(provider=user)

        return Booking.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated, IsClient]

        if self.action == "cancel":
            return [IsAuthenticated, IsBookingCustomer]

        if self.action in ["confirm", "reject"]:
            return [IsAuthenticated, IsBookingProvider]

        return [IsAuthenticated, IsCustomerOrProvider]

    def perform_create(self, serializer):
        serializer.save(
            customer=self.request.user,
            status="pending"
        )

    def destroy(self, request, *args, **kwargs):
        return Response(
            {"detail": "Bookings cannot be deleted. Use cancel instead."},
            status=status.HTTP_403_FORBIDDEN
        )
    
    #Custom Actions
    @action(detail=True, methods=["patch"])
    def cancel(self, request, pk=None):
        booking = self.get_object()

        if booking.status == "cancelled":
            return Response(
                {"detail": "Booking is already cancelled."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = "cancelled"
        booking.save()

        return Response(
            {"detail": "Booking cancelled successfully."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["patch"])
    def confirm(self, request, pk=None):
        booking = self.get_object()

        if booking.status != "pending":
            return Response(
                {"detail": "Only pending bookings can be confirmed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = "confirmed"
        booking.save()

        return Response(
            {"detail": "Booking confirmed."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["patch"])
    def reject(self, request, pk=None):
        booking = self.get_object()

        if booking.status != "pending":
            return Response(
                {"detail": "Only pending bookings can be rejected."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = "cancelled"
        booking.save()

        return Response(
            {"detail": "Booking rejected."},
            status=status.HTTP_200_OK
        )
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated, IsBookingProvider])
    def confirm(self, request, pk=None):
        booking = self.get_object()

        if booking.status != "pending":
            return Response(
                {"detail": "Only pending bookings can be confirmed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = "confirmed"
        booking.save()

        serializer = self.get_serializer(booking)
        return Response(serializer.data)
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated, IsCustomerOrProvider])
    def cancel(self, request, pk=None):
        booking = self.get_object()

        if booking.status == "cancelled":
            return Response(
                {"detail": "Booking is already cancelled."},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = "cancelled"
        booking.save()

        serializer = self.get_serializer(booking)
        return Response(serializer.data)
