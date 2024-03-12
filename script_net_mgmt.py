#!usr/bin/python3
import os

#Network manager subscribed to 3 topics from Public MQTT
os.system("mosquitto_sub -h 10.0.0.12 -t RD/veh_n/route_request &")
os.system("mosquitto_sub -h 10.0.0.12 -t RD/veh_n/priority &")
os.system("mosquitto_sub -h 10.0.0.12 -t RD/new_vehicle &")

#Network manager publishes 3 topics to Private MQTT, 1 to Public MQTT
#os.system("mosquitto_pub -t RD/veh_n/route -m 'RD/veh_n/route  message'")
#os.system("mosquitto_pub -t RD/veh_n/route_request -m 'RD/veh_n/route_request  message'")
#os.system("mosquitto_pub -t RD/veh_n/priority -m 'RD/veh_n/priority  message'")
