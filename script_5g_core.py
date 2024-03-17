#!usr/bin/python3
import os

#5G Core subscribed to 3 topics from Private MQTT
os.system("mosquitto_sub -h 10.0.0.14 -t setQoS &")
