from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone

from .models import Device, SensorData


def map_view(request):
    devices = list(Device.objects.all().values())
    return render(request, "sensors/map.html", {"devices": devices})


def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, "sensors/device_detail.html", {"device": device})


def device_data_api(request, pk):
    device = get_object_or_404(Device, pk=pk)
    data = list(device.data.order_by("timestamp").values("timestamp", "value"))
    return JsonResponse(data, safe=False)


def toggle_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.is_connected = not device.is_connected
    device.save()
    return redirect("device_detail", pk=pk)

# Create your views here.
