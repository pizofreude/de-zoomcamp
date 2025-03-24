# Description: Load taxi data from a compressed CSV file (.gz) into a Kafka topic.

import csv
import json
import time
import gzip
from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def main():
    # Kafka server and topic configuration
    server = 'localhost:9092'
    topic_name = 'green-data'
    csv_file = 'data/green_tripdata_2019-10.csv.gz'  # Path to the .gz file

    # Selected columns to filter from the CSV
    selected_columns = [
        'lpep_pickup_datetime',
        'lpep_dropoff_datetime',
        'PULocationID',
        'DOLocationID',
        'passenger_count',
        'trip_distance',
        'tip_amount'
    ]

    # Create a Kafka producer
    print("[INFO] Initializing Kafka producer...")
    producer = KafkaProducer(
        bootstrap_servers=[server],
        value_serializer=json_serializer
    )

    # Check if the producer is connected to the Kafka server
    if producer.bootstrap_connected():
        print(f"[SUCCESS] Connected to Kafka broker at {server}.")
    else:
        print(f"[ERROR] Failed to connect to Kafka broker at {server}. Please check the server configuration.")
        return

    # Start measuring time
    print(f"[INFO] Starting to process the compressed CSV file: {csv_file}")
    start_time = time.time()

    # Open the .gz file and send filtered rows to Kafka
    try:
        with gzip.open(csv_file, 'rt', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            row_count = 0

            for row in reader:
                # Filter the row to include only the selected columns
                filtered_row = {key: row[key] for key in selected_columns}

                # Send the filtered row to the Kafka topic
                producer.send(topic_name, value=filtered_row)
                row_count += 1

            print(f"[INFO] Successfully processed {row_count} rows from the compressed CSV file.")
    except FileNotFoundError:
        print(f"[ERROR] The file {csv_file} was not found. Please ensure the file exists in the specified path.")
        return
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while processing the file: {e}")
        return

    # Ensure all messages are delivered
    print("[INFO] Flushing messages to Kafka...")
    producer.flush()
    producer.close()

    # End measuring time
    end_time = time.time()

    # Calculate the time taken in seconds (rounded to a whole number)
    time_taken_seconds = round(end_time - start_time)

    # Print success message
    print(f"[SUCCESS] All data successfully sent to Kafka topic '{topic_name}' in {time_taken_seconds} seconds.")

if __name__ == "__main__":
    main()