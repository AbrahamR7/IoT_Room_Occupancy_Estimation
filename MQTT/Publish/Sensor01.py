import paho.mqtt.client as mqtt
import pandas as pd

mqttBroker = "mqtt.eclipseprojects.io"
client01 = mqtt.Client("Sensor01")
client01.connect(mqttBroker)

Data = pd.read_csv("./Data/Occupancy_Estimation.csv")
Sensor01 = Data[["S1_Temp", "S1_Light", "S1_Sound"]]

for index, record in Sensor01.iterrows():
    client01.publish("temp", record["S1_Temp"])
    client01.publish("light", record["S1_Light"])
    client01.publish("sound", record["S1_Sound"])