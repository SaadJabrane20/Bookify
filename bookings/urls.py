from django.urls import path, include
from rest_framework import routers
from .views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls