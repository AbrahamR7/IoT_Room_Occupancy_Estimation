import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))


client01 = mqtt.Client("test")
client01.connect("localhost", 1883, 60)

client01.loop_start()
client01.subscribe("sound")
client01.on_message = on_message
time.sleep(60)
client01.loop_stop()
