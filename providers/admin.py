from django.contrib import admin
from .models import WorkingHours
# Register your models here.
@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "day_of_week",
        "start_time",
        "end_time",
    )
    list_filter = ("provider", "day_of_week")