from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=2000)
print('consumer setted')

consumer.subscribe(['police.department.calls.event'])
print('subscribe setted')

for message in consumer:
    print(message.value)