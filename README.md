# Sensor Map Vibe

This project demonstrates the vibe coding to make the basic sensor mapping application built with **Django** and **Leaflet**. It shows how to display a list of sensor devices on an interactive map and visualize sensor readings when a device is selected.

## Prompt Example for vibe coding
You can use nocode tools such as OpenAI codex, bubble, nocodefusion, flutterflow et al to make new project files or update with redesign using Copilot, Cursor tools after loading them. If you have experience the software development process, you can understand it's important to define requirements as the viewpoint of user goals, needs, interface, workflow considering technical framework, components like server side (flask, django), client side(bootstrap, flutter etc). 
In example, to demonstrate the vibe coding how to create wep-based application including map, dashboard, I designed the simple UX sketches below to create the UI (User Interface) using Figma and give them to LLM.

<img src="https://github.com/mac999/sensor-map-vibe/blob/main/UX1.png?raw=true" height="300" />

- OpenAI codex: Make project and files which have title called "sensor map vibe" using python, django, leaflet map, support to visualize sensor device PoI list on map, visualize sensor data chart when user click the PoI, connect and disconnect sensor device which has (device name, MAC address, position, device number, description, dataset fields) with example data.   
- Github Copilot for map.html: Redesign and update this map.html consdering this pasted image. Use bootstrap library and style to make this UI and UX. Add resize handler to show the entire the map, charts components which are depending on browser screen size automatically, naturally. Font height = 11pt. Make PoI from Device and SensorData in models.py. Make these charts using bootstrap chart from Device and SensorData in models.py.
- Github Copilot for device_detail.html: Redesign and update this HTML consdering this pasted image. Use bootstrap library and style to make this UI and UX. Add resize handler to show the entire the map, charts components which are depending on browser screen size automatically, naturally. Font height = 11pt. Make PoI from Device and SensorData in models.py. Make these charts using bootstrap chart from Device and SensorData in models.py.
- GitHub Copilot to add click event: Add click event of Detail Sensor List menu and show the device_detail with device 1 when click it.

# Generated Result 
It generated the project files including UX like below.

<img src="https://github.com/mac999/sensor-map-vibe/blob/main/app.gif" height="300" />

There is no right answer to how to develop the projects that satisfy the needs of various users in Vibe Coding. When you Vibe Coding, you will find that you have to predict the useful prompts of your LLM as if you are predicting the project template, folders, files, code routines that are generated variably. Therefore, you should not believe what some people say that anyone can Vibe Coding without knowing anything about development or technology stack. If you have no experience with the software development process, your vibe coding projects will likely end up being limited to things like calculators, simple games, and developing simple HTML pages.

# Features

- List of sensor devices with name, MAC address, position, device number and description.
- Interactive map with markers for each device using Leaflet.
- Line chart of sensor data powered by Chart.js when viewing a device.
- Ability to toggle a device's connection status.
- Example data provided via Django fixtures.

# Setup

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
# Author
Taewook Kang, Ph.D, laputa99999@gmail.com

# License
MIT license
