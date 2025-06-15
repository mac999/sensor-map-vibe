# Sensor Map Vibe

This project demonstrates vibe coding to make the basic sensor mapping application built with **Django** and **Leaflet**. It shows how to display a list of sensor devices on an interactive map and visualize sensor readings when a device is selected.

## Prompt
Design the UX sketches below to create the UI (User Interface) and give them to LLM.

- OpenAI codex: Make project which has title called "sensor map vibe" using python, django, leaflet map, support to visualize sensor device PoI list on map, visualize sensor data chart when user click the PoI, connect and disconnect sensor device which has (device name, MAC address, position, device number, description, dataset fields) with example data.   
- Github Copilot for map.html: Redesign and update this map.html consdering this pasted image. Use bootstrap library and style to make this UI and UX. Add resize handler to show the entire the map, charts components which are depending on browser screen size automatically, naturally. Font height = 11pt. Make PoI from Device and SensorData in models.py. Make these charts using bootstrap chart from Device and SensorData in models.py.
- Github Copilot for device_detail.html: Redesign and update this HTML consdering this pasted image. Use bootstrap library and style to make this UI and UX. Add resize handler to show the entire the map, charts components which are depending on browser screen size automatically, naturally. Font height = 11pt. Make PoI from Device and SensorData in models.py. Make these charts using bootstrap chart from Device and SensorData in models.py.

## Features

- List of sensor devices with name, MAC address, position, device number and description.
- Interactive map with markers for each device using Leaflet.
- Line chart of sensor data powered by Chart.js when viewing a device.
- Ability to toggle a device's connection status.
- Example data provided via Django fixtures.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations and load example data:
   ```bash
   python manage.py migrate
   python manage.py loaddata devices.json sensordata.json
   ```
3. Run the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
4. Open `http://localhost:8000/` to see the map.

Run tests with:
```bash
python manage.py test
```

This project serves as a simple starting point for experimenting with sensor mapping and data visualization in Django.
