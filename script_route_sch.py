#!usr/bin/python3
import paho.mqtt.client as mqtt
import time

# Se definen las callback functions
def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conexión exitosa al broker MQTT")
    else:
        print("No se pudo conectar al broker MQTT, código de retorno:", reason_code)

def on_disconnect(client, userdata, flags, reason_code, properties):
        print("Disconnected from broker "+ str(reason_code))

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")

def on_publish(client, userdata, mid, reason_codes, properties):
        print("Mensaje publicado: " + str(mid))

# Crear un cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Configurar las funciones de callback
#client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# Conectar al broker MQTT
print("Connecting to broker...")
client.connect("10.0.0.12", 1883)

# Suscribir Route Scheduler a los topics
client.loop_start()
client.subscribe("veh_n/route_request")
client.subscribe("veh_n/priority")
client.subscribe("new_vehicle")
print("Suscrito a topics veh")

# Publicar mensaje en topic /route
client.publish("veh_n/route", "Actualización de ruta")
print("Mensaje publicado en el topic veh_n/route")

# Desconectar del broker MQTT a los 30 segundos
time.sleep(30)
client.disconnect()

# mosquitto_pub -t veh_n/route -m 'Mensaje de prueba de veh_n/route'
