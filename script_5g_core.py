#!usr/bin/python3
import os

#5G Core subscribed to 3 topics from Private MQTT
os.system("mosquitto_sub -h 10.0.0.13 -t RD/veh_n/route_request &")
os.system("mosquitto_sub -h 10.0.0.13 -t RD/veh_n/priority &")
os.system("mosquitto_sub -h 10.0.0.13 -t RD/veh_n/route &")
