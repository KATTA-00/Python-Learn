try:
    import paho.mqtt.client as mqtt
except:
    import pip
    pip.main(['install','paho-mqtt'])


# Imports
import time
import paho.mqtt.client as mqtt

topic_1 = "G8C/SERVER/DATA"
topic_2 = "G8C/CCC/DATA"
mqttBroker = "mqtt.eclipseprojects.io" #Must be connected to the vpn
#mqttPort = 8000
client = mqtt.Client("G8C") #Group 1A (Classified Document Room)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic_1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    return str(msg.payload.decode("utf-8"))



try:
    client.connect(mqttBroker)
    client.on_connect = on_connect
    client.on_message = on_message
    client.subscribe(topic_1)
    client.loop_start()
except:
    print("Connection to MQTT broker failed!")
    exit(1)

while True:
    print(on_message())
    # update display
    print(100)


