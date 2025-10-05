### PYSPARK KAFKA STRUCTURED STREAMING EXAMPLE

## step 1
docker compose up -d --build

## step 2
Kafka topic creation
Using CLI Producer (quick & manual)

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka:9092 --topic trips
```

•	Once it runs, you’ll get a prompt. Type one JSON message per line:

```bash
docker exec -i kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka:9092 --topic trips <<EOF
{"pickup_datetime":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","PULocationID":150,"passenger_count":3}
EOF

docker exec -i kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka:9092 --topic trips <<EOF
{"pickup_datetime":"$(date +%Y-%m-%dT%H:%M:%S)","PULocationID":10,"passenger_count":39}
EOF


docker exec -i kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka:9092 --topic trips <<EOF
{"pickup_datetime":"$(date +%Y-%m-%dT%H:%M:%S)","PULocationID":40,"passenger_count":39}
EOF


docker exec -i kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka:9092 --topic trips <<EOF
{"pickup_datetime":"$(date +%Y-%m-%dT%H:%M:%S)","PULocationID":15,"passenger_count":39}
EOF
```

## Step 3
Container Logs

```bash
docker logs -f kafka
docker logs -f pyspark
```

## Step 4
Go to Jupyter Notebook 
in pyspark container you will find a link starts with  http://127.0.0.1:8888/lab?token=

open work folder, you will find read_kaflka_topic.ipynb file, open and run it. 

for Spark UI



## Step 5
Clear 

```bash
docker rm -f kafka
docker volume rm kafka-data
```











