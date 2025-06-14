from django.contrib import admin

from .models import Device, SensorData


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "mac_address", "device_number", "is_connected")


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ("device", "timestamp", "value")
