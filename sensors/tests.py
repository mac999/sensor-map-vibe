from django.test import TestCase
from django.urls import reverse

from .models import Device


class SensorViewsTest(TestCase):
    fixtures = ["devices.json", "sensordata.json"]

    def test_map_view(self):
        response = self.client.get(reverse("map"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sensor Map Vibe")

    def test_device_detail_view(self):
        device = Device.objects.first()
        response = self.client.get(reverse("device_detail", args=[device.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, device.name)
