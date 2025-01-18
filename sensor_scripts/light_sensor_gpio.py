import board
import digitalio
import time
import json
import random

# Configure the light sensor input pin
light_sensor_pin = board.D16  # GPIO16 (pin 36)
light_sensor = digitalio.DigitalInOut(light_sensor_pin)
light_sensor.direction = digitalio.Direction.INPUT

def generate_lux_value(is_light):
    """Generate a static lux value based on whether it's light or dark, then round it."""
    if is_light:
        # Lux value for light, set to a fixed range (e.g., 2000-10000 lux) and rounded
        lux_value = round(random.uniform(2000, 10000))  # Lux range for light, rounded
    else:
        # Lux value for darkness, set to a fixed range (e.g., 0-200 lux) and rounded
        lux_value = round(random.uniform(0, 200))  # Lux range for darkness, rounded
    return lux_value

# Read sensor state once
is_light = light_sensor.value  # Check if the sensor is receiving light or darkness

# Generate lux value based on sensor state
lux_value = generate_lux_value(is_light)

# Determine status (light or darkness)
status = "light" if is_light else "darkness"

# Create data dictionary and convert it to JSON
data = {
    "lux": lux_value,
    "status": status
}

# Print JSON to stdout (or send to Node-RED)
print(json.dumps(data))
