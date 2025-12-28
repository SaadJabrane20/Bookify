from django.contrib import admin
from .models import Profile
from .models import Profile
admin.site.site_header = "Bookify Admin"
admin.site.site_title = "Bookify"
admin.site.index_title = "Manage Bookify"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "role",
        "phone_number",
        "category",
    )
    list_filter = ("role",)
    search_fields = ("user__username", "phone_number")