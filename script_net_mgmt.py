#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import threading
import sys

# Se definen las callback functions
def on_log(client, userdata, level, buf):
    print("log: "+buf)
    
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conexión exitosa al broker MQTT")
    else:
        print("No se pudo conectar al broker MQTT, código de retorno:", rc)

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
    if msg.topic =="veh_n/route":
        client_private.publish("setQoS","default")

def on_publish(client, userdata, mid, reason_codes, properties):
        print("Mensaje publicado: " + str(mid))

# Función para enviar mensajes interactivamente
def send_message(client_private):
    while True:
        message = input("Introduce el mensaje de tipo setQoS: ")
        client_private.publish("setQoS", message)
        print("Mensaje publicado en el topic setQoS")

def main():
    # Crear los clientes, uno para cada broker MQTT
    client_public = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "client_public")
    client_private = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "client_private")

    # Configurar las funciones de callback asociadas al Public MQTT
    #client_public.on_log = on_log
    client_public.on_connect = on_connect
    client_public.on_disconnect = on_disconnect
    client_private.on_subscribe = on_subscribe
    client_public.on_message = on_message

    # Configurar las funciones de callback asociadas al Private MQTT
    #client_private.on_log = on_log
    client_private.on_connect = on_connect
    client_private.on_disconnect = on_disconnect
    client_private.on_publish = on_publish

    # Conectar a los broker MQTT
    print("Connecting to Public-MQTT")
    client_public.connect("10.0.0.12", 1883)
    print("Connecting to Private-MQTT")
    client_private.connect("10.0.0.14", 1883)

    client_public.loop_start()
    client_private.loop_start()

    # Suscribir al topic route
    client_public.subscribe("veh_n/route")
    print("Suscrito a topic veh_n/route")

    # Si no se introducen los valores como parámetros se toman los siguientes valores predeterminados
    if (len(sys.argv) >= 2 and sys.argv[1] == "setQos"):
        if (len(sys.argv)==2):
            msg_QoS = "UL,20mbit,30,10"
        else:
            msg_QoS = sys.argv[2]
        client_private.publish("setQoS",msg_QoS )
        print("Mensaje publicado en el topic setQoS")

    # Iniciar el hilo para la entrada del usuario
    thread = threading.Thread(target=send_message, args=(client_private,))
    thread.start()

    # Mantener el cliente en ejecución
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Desconectando del broker MQTT...")
        client_public.loop_stop()
        client_public.disconnect()
        client_private.loop_stop()
        client_private.disconnect()

if __name__ == "__main__":
    main()
