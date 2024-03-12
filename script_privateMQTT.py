#!usr/bin/python3
import os

#Private MQTT subscribed to 3 topics from Network Manager
os.system("mosquitto_sub -h 10.0.0.11 -t RD/veh_n/route &")
os.system("mosquitto_sub -h 10.0.0.11 -t RD/veh_n/route_request &")
os.system("mosquitto_sub -h 10.0.0.11 -t RD/veh_/priority &")

#Private MQTT publishes 3 topics
#os.system("mosquitto_pub -t RD/veh_n/route -m 'RD/veh_n/route message'")
#os.system("mosquitto_pub -t RD/veh_n/route_request -m 'RD/veh_n/route_request  message'")
#os.system("mosquitto_pub -t RD/veh_n/priority -m 'RD/veh_n/priority  message'")
