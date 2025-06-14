from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('device/<int:pk>/', views.device_detail, name='device_detail'),
    path('api/device/<int:pk>/data/', views.device_data_api, name='device_data_api'),
    path('toggle/<int:pk>/', views.toggle_device, name='toggle_device'),
]
