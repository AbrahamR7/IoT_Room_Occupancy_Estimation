import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensor01")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensor01_df = Data[["Date", "Time", "S1_Temp", "S1_Light", "S1_Sound", "Room_Occupancy_Count"]]
Sensor01_modified_df = pd.DataFrame()
Sensor01_modified_df['temp'] = Sensor01_df['Date'].astype(str) + ', ' + Sensor01_df['Time'].astype(str) + ', ' + \
                               Sensor01_df['S1_Temp'].astype(str) + ', ' + "1" + ', ' + Sensor01_df[
                                   'Room_Occupancy_Count'].astype(str)
Sensor01_modified_df['light'] = Sensor01_df['Date'].astype(str) + ', ' + Sensor01_df['Time'].astype(str) + ', ' + \
                                Sensor01_df['S1_Light'].astype(str) + ', ' + "1" + ', ' + Sensor01_df[
                                    'Room_Occupancy_Count'].astype(str)
Sensor01_modified_df['sound'] = Sensor01_df['Date'].astype(str) + ', ' + Sensor01_df['Time'].astype(str) + ', ' + \
                                Sensor01_df['S1_Sound'].astype(str) + ', ' + "1" + ', ' + Sensor01_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensor01_modified_df.iterrows():
    client01.publish("temp", record["temp"])
    client01.publish("light", record["light"])
    client01.publish("sound", record["sound"])
    print(i, " message sent to MQTT server")
    time.sleep(0.1)
    i += 1
