from kafka import KafkaProducer
import json
import time
import random

from kafka.errors import KafkaError
import backoff  # You'll need to add this to requirements.txt

@backoff.on_exception(backoff.expo, KafkaError, max_tries=5)
def create_producer():
    return KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def generate_customer_data():
    return {
        "customer_id": random.randint(1, 1000),
        "name": "Customer" + str(random.randint(1, 1000)),
        "address": "Address" + str(random.randint(1, 1000)),
        "update_time": int(time.time())
    }

def generate_order_data():
    return {
        "order_id": random.randint(1, 10000),
        "customer_id": random.randint(1, 1000),
        "product_id": random.randint(1, 500),
        "quantity": random.randint(1, 10),
        "price": random.uniform(10.0, 500.0),
        "order_time": int(time.time())
    }

def main():
    producer = create_producer()
    try:
        while True:
            customer_data = generate_customer_data()
            order_data = generate_order_data()

            producer.send('customers', customer_data)
            producer.send('orders', order_data)
            print("Sent data:", customer_data, order_data)

            time.sleep(5)  # send data every 5 seconds
    except KeyboardInterrupt:
        print("Stopping producer")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
