#!usr/bin/python3
import os

#Network manager subscribed to 1 topic from Public MQTT
os.system("sudo mosquitto_sub -h 10.0.0.12 -t veh_n/route &")

#Network manager publishes 3 topics to Private MQTT, 1 to Public MQTT
#os.system("mosquitto_pub -t RD/veh_n/route -m 'RD/veh_n/route  message'")
#os.system("mosquitto_pub -t RD/veh_n/route_request -m 'RD/veh_n/route_request  message'")
#os.system("mosquitto_pub -t RD/veh_n/priority -m 'RD/veh_n/priority  message'")
