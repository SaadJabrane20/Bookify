from django.contrib import admin
from .models import Booking
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "provider",
        "service",
        "status",
        "start_time",
        "end_time"
    )

    list_filter = ("status","start_time", "end_time", "provider")
    search_fields = ("customer__username", "provider__username")

    def has_delete_permission(self, request, obj=None):
        return False