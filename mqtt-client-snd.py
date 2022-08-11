import paho.mqtt.client as mqtt
import datetime
import time
import sys


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

p = sys.argv
if len(p) < 5:
    print("Usage: python %s <broker host> <broker port> <interval> <topic>" % p[0])
    sys.exit(0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(p[1], int(p[2]), 60)
interval = float(p[3])

while(True):
    client.publish(p[4], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(interval)


