## Module 3 Homework

ATTENTION: At the end of the submission form, you will be required to include a link to your GitHub repository or other public code-hosting site. 
This repository should contain your code for solving the homework. If your solution includes code that is not in file format (such as SQL queries or 
shell commands), please include these directly in the README file of your repository.

<b><u>Important Note:</b></u> <p> For this homework we will be using the Yellow Taxi Trip Records for **January 2024 - June 2024 NOT the entire year of data** 
Parquet Files from the New York
City Taxi Data found here: </br> https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page </br>
If you are using orchestration such as Kestra, Mage, Airflow or Prefect etc. do not load the data into Big Query using the orchestrator.</br> 
Stop with loading the files into a bucket. </br></br>

**Load Script:** You can manually download the parquet files and upload them to your GCS Bucket or you can use the linked script [here](./load_yellow_taxi_data.py):<br>
You will simply need to generate a Service Account with GCS Admin Priveleges or be authenticated with the Google SDK and update the bucket name in the script to the name of your bucket<br>
Nothing is fool proof so make sure that all 6 files show in your GCS Bucket before begining.</br><br>

<u>NOTE:</u> You will need to use the PARQUET option files when creating an External Table</br>

<b>S3
 SETUP:</b></br>
Upload dataset via `python load_yellow_taxi_data_s3.py `. </br>
Prerequisite: `pip install -r requirements.txt` </br>
</p>


<b>ATHENA SETUP:</b></br>
Create an external table using the Yellow Taxi Trip Records. </br>
Create a (regular/materialized) table in BQ using the Yellow Taxi Trip Records (do not partition or cluster this table). </br>
</p>

```sql
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

```

```sql
-- Create a (regular/materialized) table in Athena using the Yellow Taxi Trip Records (do not partition or cluster this table).
CREATE TABLE dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular AS 
SELECT * FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_ext;
```


## Question 1:
Question 1: What is count of records for the 2024 Yellow Taxi Data?
- [ ] 65,623
- [ ] 840,402
- [X] 20,332,093
- [ ] 85,431,289

### Answer:
```sql
-- Query to count the records for the 2024 Yellow Taxi Data
SELECT COUNT(*) AS record_count
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular;
```


## Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.</br> 
What is the **estimated amount** of data that will be read when this query is executed on the External Table and the Table?

- [ ] 18.82 MB for the External Table and 47.60 MB for the Materialized Table
- [X] 0 MB for the External Table and 155.12 MB for the Materialized Table
- [ ] 2.14 GB for the External Table and 0MB for the Materialized Table
- [ ] 0 MB for the External Table and 0MB for the Materialized Table

### Answer:
```sql
-- Query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
SELECT COUNT(DISTINCT pulocationid) AS distinct_pulocationid_count
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_ext;

SELECT COUNT(DISTINCT pulocationid) AS distinct_pulocationid_count
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular;
```

## Question 3:
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?
- [X] BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires 
reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.
- [ ] BigQuery duplicates data across multiple storage partitions, so selecting two columns instead of one requires scanning the table twice, 
doubling the estimated bytes processed.
- [ ] BigQuery automatically caches the first queried column, so adding a second column increases processing time but does not affect the estimated bytes scanned.
- [ ] When selecting multiple columns, BigQuery performs an implicit join operation between them, increasing the estimated bytes processed

### Answer:
```sql
-- Query to retrieve the PULocationID from the table (not the external table) in BigQuery.
SELECT pulocationid
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular;
-- Data scanned:15.55 MB

-- Query to retrieve the PULocationID and DOLocationID on the same table.
SELECT pulocationid, dolocationid
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular;
-- Data scanned:34.56 MB
```

## Question 4:
How many records have a fare_amount of 0?
- [ ] 128,210
- [ ] 546,578
- [ ] 20,188,016
- [X] 8,333

### Answer:
```sql
-- Query to count the records with a fare_amount of 0
SELECT COUNT(*) AS record_count
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular
WHERE fare_amount = 0;
```

## Question 5:
What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)
- [X] Partition by tpep_dropoff_datetime and Cluster on VendorID
- [ ] Cluster on by tpep_dropoff_datetime and Cluster on VendorID
- [ ] Cluster on tpep_dropoff_datetime Partition by VendorID
- [ ] Partition by tpep_dropoff_datetime and Partition by VendorID

#### Answer:
```sql
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
```


## Question 6:
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime
2024-03-01 and 2024-03-15 (inclusive)</br>

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? </br>

Choose the answer which most closely matches.</br> 

- [ ] 12.47 MB for non-partitioned table and 326.42 MB for the partitioned table
- [X] 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
- [ ] 5.87 MB for non-partitioned table and 0 MB for the partitioned table
- [ ] 310.31 MB for non-partitioned table and 285.64 MB for the partitioned table

### Answer:
```sql
-- Query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)
SELECT DISTINCT VendorID
FROM dezoomcamp_kestra_db.yellow_taxi_trip_records_2024_regular
WHERE tpep_dropoff_datetime BETWEEN TIMESTAMP '2024-03-01 00:00:00' AND TIMESTAMP '2024-03-15 23:59:59';
--

-- Query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (optimized)
SELECT DISTINCT VendorID
FROM dezoomcamp_kestra_db.optimized_yellow_taxi_trip_records
WHERE tpep_dropoff_datetime BETWEEN TIMESTAMP '2024-03-01 00:00:00' AND TIMESTAMP '2024-03-15 23:59:59';
```


## Question 7: 
Where is the data stored in the External Table you created?

- [ ] Big Query
- [ ] Container Registry
- [X] GCP Bucket / S3 Bucket
- [ ] Big Table

## Question 8:
It is best practice in Big Query to always cluster your data:
- [ ] True
- [X] False

### Answer:
While clustering can significantly improve query performance by organizing the data to reduce the amount of data scanned, it is not always necessary or beneficial for every dataset or use case. Clustering is most useful when we frequently run queries that filter or aggregate by the clustered columns. However, clustering adds overhead to data loading and maintenance, and for small datasets or infrequently queried columns, the benefits may not outweigh the computation costs.

Therefore, it is not best practice to always cluster our data in BigQuery. Instead, we should evaluate the specific needs of our queries and data to determine whether clustering will provide significant performance benefits.

Clustering is beneficial when:
- Queries frequently filter or aggregate on specific columns.
- Datasets are large and can benefit from organized data storage.
- Improved query performance and reduced costs are desired.

Partitioning is beneficial when:
- Queries frequently filter by date or time columns.
- Datasets are large and can benefit from organized data storage.
- Improved query performance and reduced costs are desired.
- Managing data lifecycle and retention policies are necessary.


## (Bonus: Not worth points) Question 9:
No Points: Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? Why?


## Submitting the solutions

Form for submitting: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw3