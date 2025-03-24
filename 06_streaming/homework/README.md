# Homework

In this homework, we're going to learn about streaming with PyFlink.

Instead of Kafka, we will use Red Panda, which is a drop-in
replacement for Kafka. It implements the same interface, 
so we can use the Kafka library for Python for communicating
with it, as well as use the Kafka connector in PyFlink.

For this homework we will be using the Taxi data:
- Green 2019-10 data from [here](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz)


## Setup

We need:

- Red Panda
- Flink Job Manager
- Flink Task Manager
- Postgres

It's the same setup as in the [pyflink module](../../../06-streaming/pyflink/), so go there and start docker-compose:

```bash
cd ../../../06-streaming/pyflink/
docker-compose up
```

(Add `-d` if you want to run in detached mode)

Visit http://localhost:8081 to see the Flink Job Manager

Connect to Postgres with pgcli, pg-admin, [DBeaver](https://dbeaver.io/) or any other tool.

The connection credentials are:

- Username `postgres`
- Password `postgres`
- Database `postgres`
- Host `localhost`
- Port `5432`

With pgcli, you'll need to run this to connect:

```bash
pgcli -h localhost -p 5432 -u postgres -d postgres
```

Run these query to create the Postgres landing zone for the first events and windows:

```sql 
CREATE TABLE processed_events (
    test_data INTEGER,
    event_timestamp TIMESTAMP
);

CREATE TABLE processed_events_aggregated (
    event_hour TIMESTAMP,
    test_data INTEGER,
    num_hits INTEGER 
);
```

## Question 1: Redpanda version

Now let's find out the version of redpandas. 

For that, check the output of the command `rpk help` _inside the container_. The name of the container is `redpanda-1`.

Find out what you need to execute based on the `help` output.

What's the version, based on the output of the command you executed? (copy the entire version)

### Answer:

To find out the version of Redpanda, we should run the rpk help command inside the redpanda-1 container. To do this, we can use the following command in our terminal:

```bash
docker exec -it redpanda-1 rpk help
```

This will execute the rpk help command inside the redpanda-1 container.

The output of the command will provide information about the available commands and options for the rpk tool.

From the output, we can see `version` as one of the available commands. To get the version of Redpanda, we can run the following command:
```bash
docker exec -it redpanda-1 rpk version

OUTPUT:
Version:     v24.2.18
Git ref:     f9a22d4430
Build date:  2025-02-14T12:52:55Z
OS/Arch:     linux/amd64
Go version:  go1.23.1

Redpanda Cluster
  node-1  v24.2.18 - f9a22d443087b824803638623d6b7492ec8221f9
```


## Question 2. Creating a topic

Before we can send data to the redpanda server, we
need to create a topic. We do it also with the `rpk`
command we used previously for figuring out the version of 
redpandas.

Read the output of `help` and based on it, create a topic with name `green-trips` 

What's the output of the command for creating a topic? Include the entire output in your answer.

### Answer:

To create a topic with the name "green-trips" using the rpk command, we can use the following command:

```bash
docker-compose exec redpanda-1 rpk topic create green-trips

OUTPUT:
TOPIC        STATUS
green-trips  OK
```


## Question 3. Connecting to the Kafka server

We need to make sure we can connect to the server, so
later we can send some data to its topics

First, let's install the kafka connector (up to you if you
want to have a separate virtual environment for that)

```bash
pip install kafka-python
```

You can start a jupyter notebook in your solution folder or
create a script

Let's try to connect to our server:

```python
import json

from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=json_serializer
)

producer.bootstrap_connected()
```

Provided that you can connect to the server, what's the output
of the last command?

### Answer:

We created the script `question3.py` and ran it in the terminal:

```bash
python src/producers/question3.py

OUTPUT:
Producer connected: True
```

## Question 4: Sending the Trip Data

Now we need to send the data to the `green-trips` topic

Read the data, and keep only these columns:

* `'lpep_pickup_datetime',`
* `'lpep_dropoff_datetime',`
* `'PULocationID',`
* `'DOLocationID',`
* `'passenger_count',`
* `'trip_distance',`
* `'tip_amount'`

Now send all the data using this code:

```python
producer.send(topic_name, value=message)
```

For each row (`message`) in the dataset. In this case, `message`
is a dictionary.

After sending all the messages, flush the data:

```python
producer.flush()
```

Use `from time import time` to see the total time 

```python
from time import time

t0 = time()

# ... your code

t1 = time()
took = t1 - t0
```

How much time did it take to send the entire dataset and flush? 

### Answer:

We created the script `src/producers/load_taxi_data.py` and ran it in the terminal:

```bash
$ python src/producers/load_taxi_data.py
[INFO] Initializing Kafka producer...
[SUCCESS] Connected to Kafka broker at localhost:9092.
[INFO] Starting to process the compressed CSV file: data/green_tripdata_2019-10.csv.gz
[INFO] Successfully processed 476386 rows from the compressed CSV file.
[INFO] Flushing messages to Kafka...
[SUCCESS] All data successfully sent to Kafka topic 'green-trips' in 92 seconds.
```

The script took 92 seconds to send the entire dataset and flush.


## Question 5: Build a Sessionization Window (2 points)

Now we have the data in the Kafka stream. It's time to process it.

* Copy `aggregation_job.py` and rename it to `session_job.py`
* Have it read from `green-trips` fixing the schema
* Use a [session window](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/operators/windows/) with a gap of 5 minutes
* Use `lpep_dropoff_datetime` time as your watermark with a 5 second tolerance
* Which pickup and drop off locations have the longest unbroken streak of taxi trips?

### Answer:

Run this query to create the Postgres landing zone for the first events and windows:

```sql
CREATE TABLE taxi_events (
    VendorID INTEGER,
	lpep_pickup_datetime VARCHAR,
	lpep_dropoff_datetime VARCHAR,
	store_and_fwd_flag VARCHAR,
	RatecodeID INTEGER,
	PULocationID INTEGER,
	DOLocationID INTEGER,
	passenger_count INTEGER,
	trip_distance NUMERIC(10, 2),
	fare_amount NUMERIC(10, 2),
	extra NUMERIC(10, 2),
	mta_tax NUMERIC(10, 2),
	tip_amount NUMERIC(10, 2),
	tolls_amount NUMERIC(10, 2),
	ehail_fee NUMERIC(10, 2),
	improvement_surcharge NUMERIC(10, 2),
	total_amount NUMERIC(10, 2),
	payment_type INTEGER,
	trip_type INTEGER,
	congestion_surcharge NUMERIC(10, 2),
	pickup_timestamp TIMESTAMP(3)
);

CREATE UNIQUE INDEX taxi_events_uniq ON taxi_events (pickup_timestamp, PULocationID, DOLocationID);
```

We created the script `src/session_job.py` and ran it in the terminal:

```terminal
C:\workspace\de-zoomcamp\06_streaming\homework>docker compose exec jobmanager ./bin/flink run -py /opt/src/job/session_job.py --pyFiles /opt/src -d
Job has been submitted with JobID 9bbe970a646a9fb4e68612b633bf32f5
```

The job ran successfully in the Flink Job Manager. But no data was written to the Postgres database.

So we reran the load_taxi_data.py script to send the data to the Kafka topic:

```bash
(venv) AbdulHafeez@IRHAFEEZ:/c/workspace/de-zoomcamp/06_streaming/homework$ python src/producers/load_taxi_data.py
[INFO] Initializing Kafka producer...
[SUCCESS] Connected to Kafka broker at localhost:9092.
[INFO] Starting to process the compressed CSV file: data/green_tripdata_2019-10.csv.gz
[INFO] Successfully processed 476386 rows from the compressed CSV file.
[INFO] Flushing messages to Kafka...
[SUCCESS] All data successfully sent to Kafka topic 'green-trips' in 97 seconds.
```

Then, in order to answer the question: Which pickup and drop off locations have the longest unbroken streak of taxi trips?

We ran this SQL query in the Postgres database:

```sql
WITH ranked_trips AS (
    SELECT
        PULocationID,
        DOLocationID,
        pickup_timestamp,
        ROW_NUMBER() OVER (
            PARTITION BY PULocationID, DOLocationID
            ORDER BY pickup_timestamp
        ) AS trip_rank
    FROM taxi_events
),
streaks AS (
    SELECT
        PULocationID,
        DOLocationID,
        COUNT(*) AS streak_length
    FROM (
        SELECT
            PULocationID,
            DOLocationID,
            pickup_timestamp,
            trip_rank - ROW_NUMBER() OVER (
                PARTITION BY PULocationID, DOLocationID
                ORDER BY pickup_timestamp
            ) AS streak_id
        FROM ranked_trips
    ) subquery
    GROUP BY PULocationID, DOLocationID, streak_id
)
SELECT
    PULocationID,
    DOLocationID,
    MAX(streak_length) AS longest_streak
FROM streaks
GROUP BY PULocationID, DOLocationID
ORDER BY longest_streak DESC
LIMIT 1;
```

The result was: "pulocationid"/"dolocationid" = 95 with	"longest_streak" = 44


## Submitting the solutions

- Form for submitting: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw6
- Deadline: See the website

