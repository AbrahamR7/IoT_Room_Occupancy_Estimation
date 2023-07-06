import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensor02")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensor02_df = Data[["Date", "Time", "S2_Temp", "S2_Light", "S2_Sound", "Room_Occupancy_Count"]]
Sensor02_modified_df = pd.DataFrame()
Sensor02_modified_df['temp'] = Sensor02_df['Date'].astype(str) + ', ' + Sensor02_df['Time'].astype(str) + ', ' + \
                               Sensor02_df['S2_Temp'].astype(str) + ', ' + "2" + ', ' + Sensor02_df[
                                   'Room_Occupancy_Count'].astype(str)
Sensor02_modified_df['light'] = Sensor02_df['Date'].astype(str) + ', ' + Sensor02_df['Time'].astype(str) + ', ' + \
                                Sensor02_df['S2_Light'].astype(str) + ', ' + "2" + ', ' + Sensor02_df[
                                    'Room_Occupancy_Count'].astype(str)
Sensor02_modified_df['sound'] = Sensor02_df['Date'].astype(str) + ', ' + Sensor02_df['Time'].astype(str) + ', ' + \
                                Sensor02_df['S2_Sound'].astype(str) + ', ' + "2" + ', ' + Sensor02_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensor02_modified_df.iterrows():
    client01.publish("temp", record["temp"])
    client01.publish("light", record["light"])
    client01.publish("sound", record["sound"])
    print(i, " message sent to MQTT server")
    time.sleep(0.001)
    i += 1
