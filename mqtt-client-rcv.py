import paho.mqtt.client as mqtt
import datetime
import sys

def on_connect(client, userdata, flags, rc):
    print("connected with result code: %s" % str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print("%s,%s"%(str(msg.payload), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))    

p = sys.argv

if len(p) < 2:
    print("usage: python %s <broker host> <broker port>" % p[0])
    sys.exit(0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(p[1], int(p[2]), 60)
client.loop_forever()
