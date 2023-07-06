

import sys
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer

import paho.mqtt.client as mqtt
import time

client02 = mqtt.Client("light")
client02.connect("localhost", 1883, 60)

if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: value = {value:12}".format(
                topic=msg.topic(), value=msg.value().decode('utf-8')))

    topic = "light"

    def on_message(client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        producer.produce(topic, msg, callback=delivery_callback)
        print(msg)

    client02.loop_start()
    client02.subscribe("light")
    client02.on_message = on_message
    time.sleep(10000)
    client02.loop_stop()

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()





