# Introduction
IoT environment / Managing big data

The objective of this project is to simulate the collection of streaming sensor data from an IoT environment. By creating a realistic simulation, the project aims to replicate real-world challenges and provide an opportunity for practitioners to gain hands-on experience with managing big data. Throughout the project, various tools and technologies will be explored to handle and analyze the data, allowing for the introduction of a typical procedure for effectively managing large datasets. The ultimate goal is to provide a practical learning experience while showcasing different tools and the best practices for managing big data in an IoT context.

# Room Occupancy Estimation
Occupancy sensors have been widely implemented as an energy-saving method in smart buildings. An occupancy sensor is an electronic sensor that detects the presence of some object of interest such as humans or animals. Infrared, microwave, ultrasonic, and video image processing are some of the most common occupancy detecting methods. The sensors can detect motion, body heat, CO2, Noise, temperature, humidity, and particulates. The sensors are typically connected to a building’s Internet of Things (IoT) network and feed data back to building management and booking systems, which can automate lighting, HVAC, and ventilation control while also providing data for occupancy analytics systems to better understand desk usage, meeting room efficiency, and space utilization.

## Data Set Information:
#### SOURCES
The experimental testbed for occupancy estimation was deployed in a 6m Ã— 4.6m room. The setup consisted of 7 sensor nodes and one edge node in a star configuration with the sensor nodes transmitting data to the edge every 30s using wireless transceivers. No HVAC systems were in use while the dataset was being collected.
##### Attribute Information:

. Date: YYYY/MM/DD
. Time: HH:MM:SS
. Temperature: In degree Celsius
. Light: In Lux
. Sound: In Volts (amplifier output read by ADC)
. CO2: In PPM
. CO2 Slope: Slope of CO2 values taken in a sliding window
. PIR: Binary value conveying motion detection
. Room_Occupancy_Count: Ground Truth

#### COLLECTION METHODOLOGY
The data was collected for a period of 4 days in a controlled manner with the occupancy in the room varying between 0 and 3 people. The ground truth of the occupancy count in the room was noted manually.

# MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol commonly used in IoT (Internet of Things) applications. It follows a publish-subscribe model, where devices publish messages to a central broker, and other devices subscribe to specific topics to receive those messages.

In our project, you can find Python files in the MQTT_Publish directory, specifically designed for different sensors. These files are responsible for picking the relevant columns from our dataset and publishing the records one by one to specific topics on our local MQTT broker. This simulation aims to replicate the real-world scenario of sensor data publication. We have categorized the sensor data into six different topics based on IoT environment features: temperature (temp), light, sound, CO2, CO2 slope, and motion detection (PIR). By running each of these Python files, you can publish the sensor data associated with that particular sensor to the corresponding topic.
Additionally, we have included a file named test.py in the MQTT_Subscribe directory, which allows you to subscribe to a specific topic in your MQTT broker and collect the relevant data. This file enables you to receive and analyze the sensor data published on the MQTT topics.
Through this setup, we aim to accurately simulate the publication and collection of sensor data, mimicking real-world scenarios and providing an opportunity to explore the management of IoT data in an effective and practical manner.
