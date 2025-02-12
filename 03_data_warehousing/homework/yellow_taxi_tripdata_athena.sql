-- Create and external table using the Yellow Taxi Trip Records in Athena with query result location saved to S3
CREATE EXTERNAL TABLE IF NOT EXISTS dezoomcamp_kestra_db.yellow_taxi_trip_records_ext (
  vendorid INT,
  tpep_pickup_datetime TIMESTAMP,
  tpep_dropoff_datetime TIMESTAMP,
  passenger_count INT,
  trip_distance DOUBLE,
  ratecodeid INT,
  store_and_fwd_flag STRING,
  pulocationid INT,
  dolocationid INT,
  payment_type INT,
  fare_amount DOUBLE,
  extra DOUBLE,
  mta_tax DOUBLE,
  tip_amount DOUBLE,
  tolls_amount DOUBLE,
  improvement_surcharge DOUBLE,
  total_amount DOUBLE,
  congestion_surcharge DOUBLE,
  airport_fee DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://dezoomcamp-kestra-bucket-01/parquet/'
TBLPROPERTIES ('classification' = 'parquet');


-- Create a (regular/materialized) table in Athena using the Yellow Taxi Trip Records (do not partition or cluster this table).
CREATE TABLE dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular AS 
SELECT * FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_ext;


-- Create a partitioned table in Athena using the Yellow Taxi Trip Records and partition by dropoff_date.
-- bucketed by vendorid and bucket count of 10.
CREATE TABLE IF NOT EXISTS dezoomcamp_kestra_db.yellow_taxi_trip_records_partitioned
CREATE TABLE IF NOT EXISTS dezoomcamp_kestra_db.optimized_yellow_taxi_trip_records
WITH (
  format = 'PARQUET',
  external_location = 's3://dezoomcamp-kestra-bucket-01/parquet/optimized/',
  partitioned_by = ARRAY['dropoff_date'],
  bucketed_by = ARRAY['vendorid'],
  bucket_count = 10
)
AS
SELECT
    VendorID,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    PULocationID,
    DOLocationID,
  date(tpep_dropoff_datetime) AS dropoff_date
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular;