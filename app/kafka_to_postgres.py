from kafka import KafkaConsumer
import psycopg2
import json

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="kafka_data",
    user="myuser",
    password="mypassword",
    host="postgres",  # Uses Docker service name
    port=5432
)
cursor = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'customers',  # Change to 'orders' if needed
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Ensure table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id SERIAL PRIMARY KEY,
        customer_id INT,
        name TEXT,
        address TEXT,
        update_time BIGINT
    );
""")
conn.commit()

# Insert Kafka messages into PostgreSQL
for message in consumer:
    data = message.value
    cursor.execute("INSERT INTO customers (customer_id, name, address, update_time) VALUES (%s, %s, %s, %s)",
                   (data['customer_id'], data['name'], data['address'], data['update_time']))
    conn.commit()
    print(f"Inserted: {data}")

# Close connection (Won't reach this since consumer runs forever)
conn.close()
