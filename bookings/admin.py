from django.contrib import admin
from .models import Booking
# Register your models here.
admin.site.site_header = "Bookify Admin"
admin.site.site_title = "Bookify"
admin.site.index_title = "Manage Bookify"


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
    search_fields = ("customer__username", "provider__username", "service__name")
    readonly_fields = ("customer", "provider", "service", "start_time", "end_time")
    def has_delete_permission(self, request, obj=None):
        return False