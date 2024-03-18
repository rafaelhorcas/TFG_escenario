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
mqtt_client.connect("10.0.0.12", 1883)

# Route Scheduler subscribed to to 3 Topics from Public MQTT
mqtt_client.subscribe("veh_n/route_request")
mqtt_client.subscribe("veh_n/priority")
mqtt_client.subscribe("new_vehicle")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()

# Ejemplos mensajes a publicar
# mosquitto_pub -t veh_n/route -m 'veh_n/route message'

