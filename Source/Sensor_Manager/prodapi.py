from kafka import KafkaProducer
import json
kafkaipport='3.142.69.135:9092'
producer = KafkaProducer(bootstrap_servers=kafkaipport,
value_serializer=lambda v: json.dumps(v).encode('utf-8'))        
def send_message(topic,message):
    producer.send(topic, value = message)
    producer.flush()
