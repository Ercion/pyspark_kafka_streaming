import pandas as pd
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Load sample NYC Taxi data
df = pd.read_parquet("yellow_tripdata_sample.parquet")

for _, row in df.iterrows():
    event = {
        "pickup_datetime": str(row.tpep_pickup_datetime),
        "PULocationID": int(row.PULocationID),
        "passenger_count": int(row.passenger_count)
    }
    producer.send("trips", value=event)
    print("Produced:", event)
    time.sleep(0.5)