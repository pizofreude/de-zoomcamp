# Import necessary libraries
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, DataTypes, TableEnvironment, StreamTableEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.common.time import Duration

# Update the PostgreSQL Sink Table
def create_taxi_events_sink_postgres(t_env):
    table_name = 'taxi_events'
    sink_ddl = f"""
        CREATE TABLE {table_name} (
            VendorID INTEGER,
            lpep_pickup_datetime STRING,
            lpep_dropoff_datetime STRING,
            store_and_fwd_flag STRING,
            RatecodeID INTEGER,
            PULocationID INTEGER,
            DOLocationID INTEGER,
            passenger_count INTEGER,
            trip_distance DECIMAL(10, 2),
            fare_amount DECIMAL(10, 2),
            extra DECIMAL(10, 2),
            mta_tax DECIMAL(10, 2),
            tip_amount DECIMAL(10, 2),
            tolls_amount DECIMAL(10, 2),
            ehail_fee DECIMAL(10, 2),
            improvement_surcharge DECIMAL(10, 2),
            total_amount DECIMAL(10, 2),
            payment_type INTEGER,
            trip_type INTEGER,
            congestion_surcharge DECIMAL(10, 2),
            pickup_timestamp TIMESTAMP(3),
            PRIMARY KEY (pickup_timestamp, PULocationID, DOLocationID) NOT ENFORCED
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5432/postgres',
            'table-name' = '{table_name}',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        );
        """
    t_env.execute_sql(sink_ddl)
    return table_name

# Update the Kafka Source Table
def create_events_source_kafka(t_env):
    table_name = "taxi_events_source"
    source_ddl = f"""
        CREATE TABLE {table_name} (
            VendorID INTEGER,
            lpep_pickup_datetime STRING,
            lpep_dropoff_datetime STRING,
            store_and_fwd_flag STRING,
            RatecodeID INTEGER,
            PULocationID INTEGER,
            DOLocationID INTEGER,
            passenger_count INTEGER,
            trip_distance DECIMAL(10, 2),
            fare_amount DECIMAL(10, 2),
            extra DECIMAL(10, 2),
            mta_tax DECIMAL(10, 2),
            tip_amount DECIMAL(10, 2),
            tolls_amount DECIMAL(10, 2),
            ehail_fee DECIMAL(10, 2),
            improvement_surcharge DECIMAL(10, 2),
            total_amount DECIMAL(10, 2),
            payment_type INTEGER,
            trip_type INTEGER,
            congestion_surcharge DECIMAL(10, 2),
            pickup_timestamp AS TO_TIMESTAMP(lpep_pickup_datetime, 'yyyy-MM-dd HH:mm:ss'),
            WATERMARK FOR pickup_timestamp AS pickup_timestamp - INTERVAL '5' SECOND
        ) WITH (
            'connector' = 'kafka',
            'properties.bootstrap.servers' = 'redpanda-1:29092',
            'topic' = 'green-trips',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'json'
        );
        """
    t_env.execute_sql(source_ddl)
    return table_name


# Update the Query to Write to PostgreSQL
def log_processing():
    # Set up the execution environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.enable_checkpointing(10 * 1000)
    env.set_parallelism(3)

    # Set up the table environment
    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)

    # Define the watermark strategy
    watermark_strategy = (
        WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(5))  # 5-second tolerance for late events
        .with_timestamp_assigner(
            lambda event, timestamp: event['pickup_timestamp'].timestamp() * 1000  # Assign event time in milliseconds
        )
    )

    try:
        # Create Kafka source table
        source_table = create_events_source_kafka(t_env)
        # Create PostgreSQL sink table
        sink_table = create_taxi_events_sink_postgres(t_env)

        # Insert data from Kafka source into PostgreSQL sink
        t_env.execute_sql(f"""
        INSERT INTO {sink_table}
        SELECT
            VendorID,
            lpep_pickup_datetime,
            lpep_dropoff_datetime,
            store_and_fwd_flag,
            RatecodeID,
            PULocationID,
            DOLocationID,
            passenger_count,
            trip_distance,
            fare_amount,
            extra,
            mta_tax,
            tip_amount,
            tolls_amount,
            ehail_fee,
            improvement_surcharge,
            total_amount,
            payment_type,
            trip_type,
            congestion_surcharge,
            pickup_timestamp
        FROM {source_table};
        """).wait()

    except Exception as e:
        print("Writing records from Kafka to PostgreSQL failed:", str(e))


if __name__ == '__main__':
    log_processing()
