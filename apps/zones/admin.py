from django.contrib import admin

from .models import Agency, Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ["name", "zone", "created", "updated"]
