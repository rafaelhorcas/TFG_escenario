#!usr/bin/python3
import paho.mqtt.client as mqtt

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")

# Configuración del cliente MQTT
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# Asignar la función de manejo de mensajes al cliente
mqtt_client.on_message = on_message
# Conexión al broker MQTT. Especifica la dirección IP del broker MQTT y el puerto
mqtt_client.connect("10.0.0.11", 1883)

# Public MQTT subscribed to 1 topic from Route Scheduler
mqtt_client.subscribe("veh_n/route")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()

# Ejemplos mensajes a publicar
# mosquitto_pub -t veh_n/route_request -m 'veh_n/route_request message'
# mosquitto_pub -t veh_n/priority -m 'veh_n/priority message'
# mosquitto_pub -t new_vehicle -m 'new_vehicle message'
# mosquitto_pub -t veh_n/route -m 'veh_n/route message'
