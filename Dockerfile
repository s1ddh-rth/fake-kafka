FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Be explicit about copying the app directory
COPY app/ /app/

CMD ["python", "kafka_producer.py"]
