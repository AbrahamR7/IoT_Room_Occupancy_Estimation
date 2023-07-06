import paho.mqtt.client as mqtt
import pandas as pd
import time

client01 = mqtt.Client("Sensors")
client01.connect("localhost", 1883, 60)

Data = pd.read_csv("/Users/parham_r7/myProjects/IoT/Dataset/Occupancy_Estimation.csv")
Sensors_df = Data[["Date", "Time", "S5_CO2", "S5_CO2_Slope", "S6_PIR", "S7_PIR", "Room_Occupancy_Count"]]
Sensors_modified_df = pd.DataFrame()
Sensors_modified_df['co2'] = Sensors_df['Date'].astype(str) + ', ' + Sensors_df['Time'].astype(str) + ', ' + Sensors_df[
    "S5_CO2"].astype(str) + ', ' + "5" + ', ' + Sensors_df['Room_Occupancy_Count'].astype(str)
Sensors_modified_df['co2_slope'] = Sensors_df['Date'].astype(str) + ', ' + Sensors_df['Time'].astype(str) + ', ' + \
                                   Sensors_df['S5_CO2_Slope'].astype(str) + ', ' + "5" + ', ' + Sensors_df[
                                       'Room_Occupancy_Count'].astype(str)
Sensors_modified_df['pir_s6'] = Sensors_df['Date'].astype(str) + ', ' + Sensors_df['Time'].astype(str) + ', ' + \
                                Sensors_df['S6_PIR'].astype(str) + ', ' + "6" + ', ' + Sensors_df[
                                    'Room_Occupancy_Count'].astype(str)
Sensors_modified_df['pir_s7'] = Sensors_df['Date'].astype(str) + ', ' + Sensors_df['Time'].astype(str) + ', ' + \
                                Sensors_df['S7_PIR'].astype(str) + ', ' + "7" + ', ' + Sensors_df[
                                    'Room_Occupancy_Count'].astype(str)

i = 0
for index, record in Sensors_modified_df.iterrows():
    client01.publish("co2", record["co2"])
    client01.publish("co2_slope", record["co2_slope"])
    client01.publish("pir", record["pir_s6"])
    print(i, " message sent to MQTT server")
    time.sleep(0.001)
    i += 1
