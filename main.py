import paho.mqtt.client as mqtt

mqttBrocker ="https://mqtt.eclipseprojects.io/"
client01 = mqtt.Client("Sensor01")
client01.connect(mqttBrocker)