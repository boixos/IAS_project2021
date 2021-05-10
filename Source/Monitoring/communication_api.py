from kafka import KafkaConsumer
import time
import json



def monitor():
    consumer = KafkaConsumer('monitor',
    bootstrap_servers=['3.142.69.135:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=10000*6*10
    )
    for message in consumer:
        yield message.value
