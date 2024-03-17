#!usr/bin/python3
import os

#Route Scheduler subscribed to 3 topics from Public MQTT
os.system("mosquitto_sub -h 10.0.0.12 -t veh_n/route_request &")
os.system("mosquitto_sub -h 10.0.0.12 -t veh_n/priority &")
os.system("mosquitto_sub -h 10.0.0.12 -t new_vehicle &")
