import paho.mqtt.client as mqtt
import datetime
import sys

def on_connect(client, userdata, flags, rc):
    print("connected with result code: %s" % str(rc))
    #client.subscribe("outTopic")
    #client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    #sent_time = datetime.datetime.strptime(msg.payload.decode(), date_format)
    curr_time = datetime.datetime.now()
    print("%s,%s"%(curr_time.strftime(date_format), msg.payload.decode()))
    #print("%s,%s,%s"%(sent_time.strftime(date_format), curr_time.strftime(date_format), (curr_time-sent_time).total_seconds()))

p = sys.argv

if len(p) < 3:
    print("usage: python %s <broker host> <broker port> <topic>" % p[0])
    sys.exit(0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(p[1], int(p[2]))
client.subscribe(p[3])
client.loop_forever()

