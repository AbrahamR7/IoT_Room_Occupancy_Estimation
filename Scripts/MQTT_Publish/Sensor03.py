import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensor03")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensor03_df = Data[["Date", "Time", "S3_Temp", "S3_Light", "S3_Sound", "Room_Occupancy_Count"]]
Sensor03_modified_df = pd.DataFrame()
Sensor03_modified_df['temp'] = Sensor03_df['Date'].astype(str) + ', ' + Sensor03_df['Time'].astype(str) + ', ' + \
                               Sensor03_df['S3_Temp'].astype(str) + ', ' + "3" + ', ' + Sensor03_df[
                                   'Room_Occupancy_Count'].astype(str)
Sensor03_modified_df['light'] = Sensor03_df['Date'].astype(str) + ', ' + Sensor03_df['Time'].astype(str) + ', ' + \
                                Sensor03_df['S3_Light'].astype(str) + ', ' + "3" + ', ' + Sensor03_df[
                                    'Room_Occupancy_Count'].astype(str)
Sensor03_modified_df['sound'] = Sensor03_df['Date'].astype(str) + ', ' + Sensor03_df['Time'].astype(str) + ', ' + \
                                Sensor03_df['S3_Sound'].astype(str) + ', ' + "3" + ', ' + Sensor03_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensor03_modified_df.iterrows():
    client01.publish("temp", record["temp"])
    client01.publish("light", record["light"])
    client01.publish("sound", record["sound"])
    print(i, " message sent to MQTT server")
    time.sleep(0.001)
    i += 1
