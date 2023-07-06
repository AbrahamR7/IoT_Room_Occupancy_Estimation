#!/bin/bash

CONFIG_FILE="/Users/parham_r7/myProjects/IoT/Scripts/Bridge/config.ini"

python MQTT-Confluent-Bridge-co2.py $CONFIG_FILE &
python MQTT-Confluent-Bridge-co2_slope.py $CONFIG_FILE &
python MQTT-Confluent-Bridge-light.py $CONFIG_FILE &
python MQTT-Confluent-Bridge-pir.py $CONFIG_FILE &
python MQTT-Confluent-Bridge-sound.py $CONFIG_FILE &
python MQTT-Confluent-Bridge-temp.py $CONFIG_FILE &
