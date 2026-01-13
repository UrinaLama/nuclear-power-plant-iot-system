import os
import csv
import random
import logging
import time

import paho.mqtt.client as mqtt

csv_dir = 'data/'

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def get_csv():
    csv_files = [
        f for f in os.listdir(csv_dir)
        if f.endswith('.csv')
    ]

    if not csv_files:
        logging.error("No csv files found")

    weights = [
        3 if f == 'normal.csv' else 1
        for f in csv_files
    ]

    return random.choices(csv_files, weights=weights, k=1)[0]


def publish(client, csv_path):
    with open(csv_path, 'r') as f:
        source = os.path.basename(csv_path).replace('.csv', '')  # normal / loca
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader):
            for key, val in row.items():
                if key == 'time':
                    continue

                topic = f"{os.getenv('MQTT_TOPIC', 'npp/reactor-coolant')}/{key}"

                client.publish(topic, val)
                logging.info(f"Published [{source}] {topic}: {val}")
            time.sleep(5)


def simulate():
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        'simulator',
    )

    client.on_connect = on_connect
    client.connect(
        host=os.getenv('MQTT_HOST', 'npp-mosquitto'),
        port=int(os.getenv('MQTT_PORT', '1883')),
        keepalive=60
    )

    client.loop_start()

    try:
        while True:
            csv_file = get_csv()
            csv_path = os.path.join(csv_dir, csv_file)

            publish(client, csv_path)
    except Exception as e:
        logging.error("Connection was interrupted: {}", e)
        client.disconnect()
        client.loop_stop()
        exit(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    simulate()
