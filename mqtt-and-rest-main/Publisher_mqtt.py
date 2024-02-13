
from time import sleep
import paho.mqtt.client as mqtt
from datetime import datetime
import psutil,json
import uuid, time


# Create a new MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect('mqtt.eclipseprojects.io', 1883)

# Publish a message to a topic. Use your studend ID as topic
# for i in range(10):
#     client.publish('s305979', f'Hello World {i}!')
#     sleep(1)

mac = str(hex(uuid.getnode()))  # creating time series mac:battery
# mac = '0xb3aca3081d12'
# print("mac: ", mac)
while(True):
    battery = psutil.sensors_battery()
    battery_percentage = int(battery.percent)
    pluged_in = int(battery.power_plugged)
    timestamp_ms = int(time.time() * 1000) 
    # print(battery)
    # print(battery_percentage, pluged_in)

    to_json = {'mac_address':mac, 'timestamp': timestamp_ms, 'battery_level': battery_percentage, 'power_plugged': pluged_in}
    to_json = json.dumps(to_json)
    # print(to_json)
    # print(type(to_json))
    sleep(1)
    # print(to_json)
    client.publish('s305979', to_json)