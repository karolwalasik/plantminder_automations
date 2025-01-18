import adafruit_dht
import board
import json

# Ustaw GPIO dla DHT11
dht_device = adafruit_dht.DHT11(board.D4)

try:
    temperature = dht_device.temperature
    humidity = dht_device.humidity

    # Tworzenie danych w formacie JSON
    data = {
        "temperature": temperature,
        "humidity": humidity
    }

    # Wypisywanie danych JSON na stdout
    print(json.dumps(data))

except RuntimeError as error:
    # Wypisywanie błędów
    print(json.dumps({"error": str(error)}))

