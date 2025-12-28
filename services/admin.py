from django.contrib import admin
from .models import Service, ServiceCategory
# Register your models here.
admin.site.site_header = "Bookify Admin"
admin.site.site_title = "Bookify"
admin.site.index_title = "Manage Bookify"


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "provider",
        "category",
        "price",
        "duration",
    )
    list_filter = ("category",)
    search_fields = ("name", "provider__username")