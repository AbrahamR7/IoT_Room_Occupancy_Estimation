import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensor07")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensors_df = Data[["Date", "Time", "S7_PIR", "Room_Occupancy_Count"]]
Sensors_modified_df = pd.DataFrame()
Sensors_modified_df['pir_s7'] = Sensors_df['Date'].astype(str) + ', ' + Sensors_df['Time'].astype(str) + ', ' + \
                                Sensors_df['S7_PIR'].astype(str) + ', ' + "7" + ', ' + Sensors_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensors_modified_df.iterrows():
    client01.publish("pir", record["pir_s7"])
    print(i, " message sent to MQTT server")
    time.sleep(0.1)
    i += 1
