import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensor04")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensor04_df = Data[["Date", "Time", "S4_Temp", "S4_Light", "S4_Sound", "Room_Occupancy_Count"]]
Sensor04_modified_df = pd.DataFrame()
Sensor04_modified_df['temp'] = Sensor04_df['Date'].astype(str) + ', ' + Sensor04_df['Time'].astype(str) + ', ' + \
                               Sensor04_df['S4_Temp'].astype(str) + ', ' + "4" + ', ' + Sensor04_df[
                                   'Room_Occupancy_Count'].astype(str)
Sensor04_modified_df['light'] = Sensor04_df['Date'].astype(str) + ', ' + Sensor04_df['Time'].astype(str) + ', ' + \
                                Sensor04_df['S4_Light'].astype(str) + ', ' + "4" + ', ' + Sensor04_df[
                                    'Room_Occupancy_Count'].astype(str)
Sensor04_modified_df['sound'] = Sensor04_df['Date'].astype(str) + ', ' + Sensor04_df['Time'].astype(str) + ', ' + \
                                Sensor04_df['S4_Sound'].astype(str) + ', ' + "4" + ', ' + Sensor04_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensor04_modified_df.iterrows():
    client01.publish("temp", record["temp"])
    client01.publish("light", record["light"])
    client01.publish("sound", record["sound"])
    print(i, " message sent to MQTT server")
    time.sleep(0.01)
    i += 1
