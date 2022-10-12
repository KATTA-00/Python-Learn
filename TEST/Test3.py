try:
    import paho.mqtt.client as mqtt
except:
    import pip

    pip.main(['install', 'paho-mqtt'])

# Imports
import time
import paho.mqtt.client as mqtt

client_publish_name = "G7BP"
client_receive_name = "G7BR"
topic_publish = "G7B/PO/DATA/IN"
topic_receive = "G7B/PO/DATA/OUT"
mqttBroker = "vpn.ce.pdn.ac.lk"
mqttPort = 8883

class Msg:
    def __init__(self):
        self.MSG_RECEIVE = ""
MSG_RECEIVE = Msg()


def on_connect_publish(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic_publish)

def on_connect_receive(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic_receive)

def on_message_publish(client, userdata, msg):
    pass

def on_message_receive(client, userdata, msg):
    MSG_RECEIVE.MSG_RECEIVE = str(msg.payload.decode("utf-8"))

OutClient = mqtt.Client(client_publish_name)
InClient = mqtt.Client(client_receive_name)

try:
    OutClient.connect(mqttBroker, mqttPort)
    InClient.connect(mqttBroker, mqttPort)
    OutClient.on_connect = on_connect_publish
    InClient.on_connect = on_connect_receive
    OutClient.on_message = on_message_publish
    InClient.on_message = on_message_receive
    OutClient.loop_start()
    InClient.loop_start()
except:
    print("Connection to MQTT broker failed!")
    exit(1)


LOCKDOWN = False
Temp_right = False
Panic_msg = ''
FLag = False
PANIC = False
tempRange = (0, 40)

while True:
    if MSG_RECEIVE.MSG_RECEIVE == '' :
        continue
    LOCK, TEMP, PANIC_STATUS = MSG_RECEIVE.MSG_RECEIVE.split(',')
    if LOCK == 'True':
        LOCK = True
    else:
        LOCK = False
    if PANIC_STATUS =='True':
        PANIC_STATUS = True
    else:
        PANIC_STATUS = False
    TEMP = float(TEMP)
    #print(MSG_RECEIVE.MSG_RECEIVE)


    if LOCK:
        if not FLag:
            FLag = True
            LOCKDOWN = True
    else:
        FLag = False

    if tempRange[0] <= TEMP <= tempRange[1]:
        Temp_right = True
    else:
        Temp_right = False

    if PANIC_STATUS and not LOCKDOWN:
        Panic_msg = "Panic Botton is pressed"
        LOCKDOWN = True
    elif LOCKDOWN:
        Panic_msg = "LOCKDOWN"
    else:
        Panic_msg = "Panic Botton is not pressed"

    ARR =  [str(LOCKDOWN),str(Temp_right),Panic_msg]
    main_string = ','.join(ARR)
    OutClient.publish(topic_publish, main_string)
    print(main_string)
