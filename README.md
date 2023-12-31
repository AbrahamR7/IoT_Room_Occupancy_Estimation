## Introduction

The objective of this project is to simulate the collection of streaming sensor data from an IoT environment. By creating a realistic simulation, the project aims to replicate real-world challenges and provide an opportunity for practitioners to gain hands-on experience with managing big data. Throughout the project, various tools and technologies will be explored to handle and analyze the data, allowing for the introduction of a typical procedure for effectively managing large datasets.

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

For those seeking an alternative to Kafka Confluent, Apache Kafka serves as a robust and freely available option. As an open-source distributed streaming platform, Apache Kafka offers a comprehensive set of features and capabilities similar to Confluent Kafka.

## MQTT Brokers and Kafka Integration

To build a high-performance data pipeline, store large volumes of data to databases, and integrate business applications in real time, Kafka is a suitable choice. It provides scalable, distributed messaging capabilities and is designed for handling high-throughput data streams. On the other hand, if you have numerous small applications or devices exchanging messages in real time across multiple channels, MQTT is a lightweight messaging protocol that fits well. However, for integrating IoT devices with backend applications and datacenters, and enabling data monitoring, control, and analysis, a combination of MQTT broker and Kafka can be leveraged, allowing seamless data flow and integration across the IoT ecosystem and backend infrastructure.


To achieve decentralized control over data flows, enabling error handling and troubleshooting, a decoupled approach is employed in bridging MQTT broker and Kafka. The project includes a "Bridge" directory consisting of multiple Python files, each dedicated to establishing a bridge between a specific MQTT broker topic and its corresponding topic on the Kafka server. To establish the connection, you can utilize the "run.sh" bash script located in the Bridge directory, which concurrently runs all the Python files. Once the connection is established, any data published on the MQTT broker will be automatically sent to the Kafka server, facilitating seamless data transfer between the two systems. This decentralized approach enhances flexibility and scalability in managing data flows while providing effective control and monitoring capabilities.

## Databricks, Spark and Delta lake 

Databricks is a cloud-based data analytics platform that provides a collaborative environment for big data processing and advanced analytics. It is tightly integrated with Apache Spark, an open-source distributed computing system renowned for its speed and versatility. Databricks simplifies the deployment and management of Spark clusters, allowing data scientists and engineers to focus on extracting insights from vast datasets.In this project, we are utilizing Databricks Community Version, which provides a single node setup, ideal for educational purposes. While it may not offer the full power of cluster processing like the enterprise version, it serves as a suitable choice for our project, allowing us to leverage the collaborative environment, notebook-based development, and distributed data processing capabilities provided by Databricks.


Delta Lake is an open-source storage layer that brings reliability, performance, and scalability to data lakes in Databricks. It enhances the functionality of data lakes by providing ACID (Atomicity, Consistency, Isolation, Durability) transactions, schema enforcement, and data versioning capabilities. Delta Lake enables organizations to build robust and trustworthy data pipelines by ensuring data integrity, enabling rollbacks, and simplifying data quality management. 

The Databricks notebook in the project serves as a "Hello World" introduction to big data management, showcasing key concepts and techniques in a practical manner.

## Structured Streaming

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. You can express your streaming computation the same way you would express a batch computation on static data. The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive. Structured Streaming provides a unified batch and streaming API that enables us to view data published to Kafka as a DataFrame.

The first step is to specify the location of our Kafka cluster and which topic we are interested in reading from. Spark allows you to read an individual topic, a specific set of topics, a regex pattern of topics, or even a specific set of partitions belonging to a set of topics. In my project databricks notebook you will find Kafka, an streaming DataFrame subscribed to all the topics. Then streaming data can be easily stored in a Delta Lake using the writeStream function in Databricks. 

In real-world scenarios, the data stored in a Delta Lake can be used for a wide range of purposes. Companies can perform data analysis and generate insights, monitor business performance, detect anomalies, identify patterns, and make data-driven decisions. Enabling real-time reporting, dashboarding, and data visualization, the data in Delta Lake can be integrated with other systems and applications.

In our case, by Creating anothe streaming DataFrame, we can read data from the Delta Lake with the ability to perform partition filtering, ensuring efficient retrieval of the desired data.

## Data Dnalysis and Machine Learning

Spark offers robust data analysis capabilities, including advanced analytics, machine learning, and graph processing. Databricks, provides convenient built-in visualization tools for data exploration and visualization. In our case, we create tables based on specific sensors and topics. By visualizing the sensor measurements against the target variable, which represents the number of people in the room, we aim to gain insights into the impact of various topics such as temperature, light, or sound on the target variable. This analysis helps us understand the relationship between sensor measurements and the target variable and identify any patterns or correlations that may exist.

<img width="1945" alt="Screenshot 2023-07-08 at 01 36 09" src="https://github.com/AbrahamR7/IoT_Room_Occupancy_Estimation/assets/119547831/204bb3d1-b1e2-47d1-b077-b580f49ef736">

<img width="1951" alt="Screenshot 2023-07-08 at 01 26 31" src="https://github.com/AbrahamR7/IoT_Room_Occupancy_Estimation/assets/119547831/08ff320d-c547-4873-8a72-e8bdb583e834">

Finally, we have created a pipeline using various algorithms available in Spark ML. The pipeline consists of stages including feature assembling, scaling, and the selected algorithm. For each algorithm, we fit the pipeline to the training data and generate predictions on the test data. We utilize the MulticlassClassificationEvaluator to evaluate the accuracy of the predictions. The accuracy of each algorithm is printed to assess its performance in predicting the number of people in the room. This pipeline allows us to explore different algorithms and identify the most accurate model for our specific dataset.

<img width="1476" alt="Screenshot 2023-07-08 at 01 40 23" src="https://github.com/AbrahamR7/IoT_Room_Occupancy_Estimation/assets/119547831/4d3106f1-fc59-4d37-9451-899e83de7d31">



