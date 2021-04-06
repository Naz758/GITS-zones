from django.contrib import admin

from .models import Agency, Profile, Role, Zone


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name", "email", "role", "ext"]


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ["name", "zone", "created", "updated"]
