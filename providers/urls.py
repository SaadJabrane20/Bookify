from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkingHoursViewSet

router = DefaultRouter()
router.register(r'providers', WorkingHoursViewSet)
urlpatterns = router.urls