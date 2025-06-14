# Sensor Map Vibe

This project demonstrates a basic sensor mapping application built with **Django** and **Leaflet**. It shows how to display a list of sensor devices on an interactive map and visualize sensor readings when a device is selected.

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
