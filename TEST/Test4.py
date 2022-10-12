try:
    from pyfirmata import Arduino, util
    import paho.mqtt.client as mqtt
except:
    import pip

    pip.main(['install', 'pyfirmata', 'paho-mqtt'])
    from pyfirmata import Arduino, util

# Imports 
import time
import paho.mqtt.client as mqtt

# Setup
group = "G7B"
topic = "G7B/PO/DATA"
mqttBroker = "vpn.ce.pdn.ac.lk"  # Must be connected to the vpn
mqttPort = 8883


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client(group)  # Group 1A (Classified Document Room)

try:
    client.connect(mqttBroker, mqttPort)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start()
except:
    print("Connection to MQTT broker failed!")
    exit(1)

# Loop
while True:
    data = "vvvvvvvvvvvvvvvvvvvvv"
    client.publish(topic, data)  # publish the data to MQTT broker using the topic
    print('Sent from Arduino ', data)
