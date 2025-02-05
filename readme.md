# **Ecommerce Data Pipeline (Kafka + PostgreSQL + PySpark)**

A simple **data pipeline** that simulates **Kafka producers**, stores messages in **PostgreSQL**, and enables **PySpark** for further data analysis.

---

## **🚀 Features**
- ✅ **Kafka Producer** generates fake **customer & order data** at regular intervals.
- ✅ **Kafka Broker** holds messages in **topics (`customers`, `orders`)**.
- ✅ **Kafka Consumer** writes data **from Kafka to PostgreSQL**.
- ✅ **Jupyter Notebook + PySpark** for **data analysis**.
- ✅ **Kafdrop (Kafka UI)** for **monitoring Kafka topics**.

---

## **🛠 Setup Instructions**

### **1️⃣ Start All Services**
To start **Kafka, Zookeeper, PostgreSQL, and Jupyter Notebook**, run:
```bash
docker-compose up -d --build
```
📌 **After running this:**
- Kafka & Zookeeper **should be running**.
- PostgreSQL **should be accessible**.
- Jupyter Notebook will be available at **[localhost:8888](http://localhost:8888)**.

### **2️⃣ Verify Kafka Broker & Producer Logs**
Check if Kafka is running fine:
```bash
docker logs kafka
```
Check if the producer is running:
```bash
docker logs kafka-producer
```

---

## **📩 Consuming Messages from Kafka**
To **check messages inside Kafka topics**, use:

📌 **Read `customers` topic messages**:
```bash
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic customers --from-beginning
```
📌 **Read `orders` topic messages**:
```bash
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic orders --from-beginning
```

---

## **📥 Writing Kafka Messages to PostgreSQL**
The **Kafka Consumer** stores messages in **PostgreSQL**.

To run the consumer that **writes Kafka messages to PostgreSQL**, execute:
```bash
docker-compose run --rm kafka-producer python app/kafka_to_postgres.py
```
📌 **Data is written in real-time to PostgreSQL!**

To verify, **connect to PostgreSQL** and check records:
```bash
docker exec -it postgres psql -U myuser -d kafka_data
```
Once inside the `psql` shell, run:
```sql
SELECT * FROM customers LIMIT 10;
SELECT * FROM orders LIMIT 10;
```

---

## **📊 Analyzing Data Using PySpark**
To analyze the data with **PySpark inside Jupyter Notebook**, follow these steps:

1. Open Jupyter Notebook at **[localhost:8888](http://localhost:8888)**
2. Install PostgreSQL connector inside Jupyter:
```python
!pip install psycopg2-binary
```
3. Run SQL queries from Jupyter:
```python
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="kafka_data",
    user="myuser",
    password="mypassword",
    host="postgres",
    port=5432
)

df = pd.read_sql("SELECT * FROM customers", conn)
df.head()
```

---

## **📡 Kafka UI - Kafdrop**
To **monitor Kafka topics in a web UI**, access **Kafdrop**:
🔗 **[http://localhost:9000](http://localhost:9000)**

- View Kafka **topics (`customers`, `orders`)**.
- Inspect messages, partitions, and offsets.

---

## **🛑 Stopping the Services**
To **stop all running containers**, use:
```bash
docker-compose down
```
📌 **This will stop Kafka, PostgreSQL, and all dependent services.**

---

## **🛠 Debugging Issues**

🔹 **Check running containers**:
```bash
docker ps
```
🔹 **Check logs for errors**:
```bash
docker logs kafka
docker logs kafka-producer
docker logs postgres
```
🔹 **Restart services**:
```bash
docker-compose down
docker-compose up -d --build
```

---

## **📌 Future Enhancements**
- Add **Kafka Streams** for real-time processing.
- Implement **Docker networking** for external connections.
- Store **processed data in a data lake (S3, HDFS, etc.)**.

---

## **👨‍💻 Author**
Maintained by **Siddharth**. Contributions welcome! 🚀

