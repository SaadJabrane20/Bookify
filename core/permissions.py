from rest_framework import permissions
from bookings.models import Booking

class IsProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only allow access if user is a provider
        return request.user.profile.role == 'provider'


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only allow clients to create bookings
        return request.user.profile.role == 'client'


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Owner check for Booking model (customer = request.user)
        if isinstance(obj, Booking):
            return obj.customer == request.user
        return False

class IsBookingCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user


class IsBookingProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.provider == request.user


class IsCustomerOrProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.customer == request.user
            or obj.provider == request.user
        )