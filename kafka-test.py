from kafka import KafkaProducer, KafkaConsumer

# Create Kafka consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

# Produce and send message after consumer is ready
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test-topic', b'Hello, Kafka from Python!')
producer.flush()
producer.close()

print("Message sent to Kafka topic 'test-topic'.")

# Consume messages from the topic
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
    break  # Stop after receiving the first message