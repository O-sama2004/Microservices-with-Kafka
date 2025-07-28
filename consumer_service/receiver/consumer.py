# consumer_service/receiver/consumer.py

from kafka import KafkaConsumer
import json

def start_consumer():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Listening to Kafka...")

    for message in consumer:
        print(f"Received: {message.value}")
        # You can add more processing logic here
