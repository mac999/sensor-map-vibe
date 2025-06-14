from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17)
    latitude = models.FloatField()
    longitude = models.FloatField()
    device_number = models.IntegerField()
    description = models.TextField(blank=True)
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SensorData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="data")
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.device.name} at {self.timestamp}"
