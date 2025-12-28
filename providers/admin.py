from django.contrib import admin
from .models import WorkingHours
# Register your models here.
admin.site.site_header = "Bookify Admin"
admin.site.site_title = "Bookify"
admin.site.index_title = "Manage Bookify"


@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "day_of_week",
        "start_time",
        "end_time",
    )

    list_filter = ("day_of_week",)
    search_fields = ("provider__username",)