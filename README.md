## Introduction
IoT environment / Managing big data

The objective of this project is to simulate the collection of streaming sensor data from an IoT environment. By creating a realistic simulation, the project aims to replicate real-world challenges and provide an opportunity for practitioners to gain hands-on experience with managing big data. Throughout the project, various tools and technologies will be explored to handle and analyze the data, allowing for the introduction of a typical procedure for effectively managing large datasets. The ultimate goal is to provide a practical learning experience while showcasing different tools and the best practices for managing big data in an IoT context.

## Room Occupancy Estimation
Occupancy sensors have been widely implemented as an energy-saving method in smart buildings. An occupancy sensor is an electronic sensor that detects the presence of some object of interest such as humans or animals. Infrared, microwave, ultrasonic, and video image processing are some of the most common occupancy detecting methods. The sensors can detect motion, body heat, CO2, Noise, temperature, humidity, and particulates. The sensors are typically connected to a building’s Internet of Things (IoT) network and feed data back to building management and booking systems, which can automate lighting, HVAC, and ventilation control while also providing data for occupancy analytics systems to better understand desk usage, meeting room efficiency, and space utilization.

### Data Set Information:
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

##### COLLECTION METHODOLOGY
The data was collected for a period of 4 days in a controlled manner with the occupancy in the room varying between 0 and 3 people. The ground truth of the occupancy count in the room was noted manually.

## MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol commonly used in IoT (Internet of Things) applications. It follows a publish-subscribe model, where devices publish messages to a central broker, and other devices subscribe to specific topics to receive those messages.

For testing or prototyping, you can use public MQTT brokers like Eclipse Mosquitto and HiveMQ. EMQ X offers a free community edition for private MQTT deployment.

In the project, you can find Python files in the MQTT_Publish directory, specifically designed for different sensors. These files are responsible for picking the relevant columns from our dataset and publishing the records one by one to specific topics on our local MQTT broker. This simulation aims to replicate the real-world scenario of continuous, real-time streams. We have categorized the sensor data into six different topics based on IoT environment features: temperature (temp), light, sound, CO2, CO2 slope, and motion detection (PIR). By running each of these Python files, you can publish the sensor data associated with that particular sensor to the corresponding topic.

Additionally, we have included a file named test.py in the MQTT_Subscribe directory, which allows you to subscribe to a specific topic in your MQTT broker and collect the relevant data. This file enables you to receive and analyze the sensor data published on the MQTT topics.

Through this setup, we aim to accurately simulate the publication and collection of sensor data, mimicking real-world scenarios and providing an opportunity to explore the management of IoT data in an effective and practical manner.

##  Kafka Confluent

A powerful and scalable streaming platform that provides a distributed messaging system capable of handling high-throughput data streams. Built on top of Apache Kafka, Confluent offers additional enterprise features and tools to simplify the management and integration of Kafka into various applications and environments.

In the Confluent_python_client directory, you will find Python client applications which produce and consume messages from an Apache Kafka cluster. If you do not have an existing cluster to use, the easiest way to run Kafka is with Confluent Cloud. New signups receive $400 to spend within Confluent Cloud during their first 60 days. Events in Kafka are organized and durably stored in named topics. When using Confluent Cloud, you can use the Confluent Cloud Console to create a topic. The topics created in Kafka Confluent for the project align with the concept of topics in MQTT brokers, However it's important to note that they differ in how they handle and manage these topics. In Kafka, topics are used for organizing and distributing streams of records, enabling producers to publish messages and consumers to subscribe and consume them. MQTT brokers, on the other hand, use topics as channels for publishing and subscribing to messages.

For those seeking an alternative to Kafka Confluent, Apache Kafka serves as a robust and freely available option. As an open-source distributed streaming platform, Apache Kafka offers a comprehensive set of features and capabilities similar to Confluent Kafka. With its high-throughput, fault-tolerant architecture, Apache Kafka enables seamless data streaming, making it an ideal choice for building scalable and real-time data pipelines, event-driven architectures, and streaming applications. 

## MQTT Brokers and Kafka Integration

To build a high-performance data pipeline, store large volumes of data to databases, and integrate business applications in real time, Kafka is a suitable choice. It provides scalable, distributed messaging capabilities and is designed for handling high-throughput data streams. On the other hand, if you have numerous small applications or devices exchanging messages in real time across multiple channels, MQTT is a lightweight messaging protocol that fits well. However, for integrating IoT devices with backend applications and datacenters, and enabling data monitoring, control, and analysis, a combination of MQTT broker and Kafka can be leveraged, allowing seamless data flow and integration across the IoT ecosystem and backend infrastructure.


To achieve decentralized control over data flows, enabling error handling and troubleshooting, a decoupled approach is employed in bridging MQTT broker and Kafka. The project includes a "Bridge" directory consisting of multiple Python files, each dedicated to establishing a bridge between a specific MQTT broker topic and its corresponding topic on the Kafka server. To establish the connection, you can utilize the "run.sh" bash script located in the Bridge directory, which concurrently runs all the Python files. Once the connection is established, any data published on the MQTT broker will be automatically sent to the Kafka server, facilitating seamless data transfer between the two systems. This decentralized approach enhances flexibility and scalability in managing data flows while providing effective control and monitoring capabilities.


