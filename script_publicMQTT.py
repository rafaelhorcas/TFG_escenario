#!usr/bin/python3
import os

#Public MQTT subscribed to 1 topic from Route Scheduler
os.system("sudo mosquitto_sub -h 10.0.0.11 -t veh_n/route &")

#Public MQTT publishes 3 topics to Route Scheduler
#os.system("mosquitto_pub -t RD/veh_n/route_request -m 'RD/veh_n/route_request message'")
#os.system("mosquitto_pub -t RD/veh_n/priority -m 'RD/veh_n/priority message'")
#os.system("mosquitto_pub -t RD/new_vehicle -m 'RD/new_vehicle message'")
