import json
from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=json_serializer
)

# Check if the producer is connected to the Kafka server
is_connected = producer.bootstrap_connected()

# Print the output of the last command
print(f"Producer connected: {is_connected}")