# Homework Week 1

**Module 1 Homework: Docker & SQL Description**

This homework module covers two main topics: Docker and SQL. The objectives are to prepare the environment, practice Docker, and practice SQL. The tasks involve:

* Running Docker in interactive mode and executing SQL and shell commands
* Understanding Docker networking and Docker Compose
* Working with Postgres database and loading data
* Analyzing trip data using SQL queries
* Using Terraform to create resources in GCP

The homework consists of 7 questions, each with specific tasks and objectives.

## Question 1. Understanding docker first 
Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

What's the version of pip in the image?

- [X] 24.3.1
- [ ] 24.2.1
- [ ] 23.3.1
- [ ] 23.2.1

### **Step-by-Step Solution**

1. **Run the Docker Container in Interactive Mode:**
Use the **`docker run`** command to start a container from the **`python:3.12.8`** image in interactive mode.
    
    ```bash
    docker run -it --entrypoint bash python:3.12.8
    
    ```
    
2. **Check the `pip` Version:**
Once inside the container, we can check the version of **`pip`** by running:
    
    ```bash
    pip --version
    
    ```
    
    Alternatively, we can use:

    ```bash
    pip -V
    ```


## Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

```yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

- [ ] postgres:5433
- [ ] localhost:5432
- [ ] db:5433
- [ ] postgres:5432
- [X] db:5432


If there are more than one answers, select only one of them.

### **Step-by-Step Solution**
- **Hostname:** Since the PostgreSQL service is named **`db`**, pgAdmin should use **`db`** as the hostname to connect to the PostgreSQL database.
- **Port:** Inside the Docker network, the PostgreSQL service is accessible on its default port **`5432`**.

Therefore, the correct **`hostname`** and **`port`** that **`pgadmin`** should use to connect to the PostgreSQL database is:

- **db:5432**

##  Prepare Postgres

Run Postgres and load data as shown in the videos. We'll use the green taxi trips from October 2019:

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
```

You will also need the dataset with zones:

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

Download this data and put it into Postgres.

You can use the code from the course. It's up to you whether
you want to use Jupyter or a python script.

## Question 3. Trip Segmentation Count

During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, **respectively**, happened:
1. Up to 1 mile
2. In between 1 (exclusive) and 3 miles (inclusive),
3. In between 3 (exclusive) and 7 miles (inclusive),
4. In between 7 (exclusive) and 10 miles (inclusive),
5. Over 10 miles 

Answers:

- [ ] 104,802;  197,670;  110,612;  27,831;  35,281
- [ ] 104,802;  198,924;  109,603;  27,678;  35,189
- [ ] 104,793;  201,407;  110,612;  27,831;  35,281
- [ ] 104,793;  202,661;  109,603;  27,678;  35,189
- [X] 104,838;  199,013;  109,645;  27,688;  35,202

### Solution:
- Up to 1 mile:
  
    ```sql
    SELECT
        COUNT(*)
    FROM
        public.green_taxi_data
    WHERE
        lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
    AND trip_distance <= 1;

    ```


- In between 1 (exclusive) and 3 miles (inclusive):
  
    ```sql
    SELECT
        COUNT(*)
    FROM
        public.green_taxi_data
    WHERE
        lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
        AND trip_distance > 1 AND trip_distance <= 3;
    ```

- In between 3 (exclusive) and 7 miles (inclusive):
    
    ```sql
    SELECT
        COUNT(*)
    FROM
        public.green_taxi_data
    WHERE
        lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
        AND trip_distance > 3 AND trip_distance <= 7;
    ```

- In between 7 (exclusive) and 10 miles (inclusive):
      
    ```sql
    SELECT
        COUNT(*)
    FROM
        public.green_taxi_data
    WHERE
        lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
        AND trip_distance > 7 AND trip_distance <= 10;
    ```

- Over 10 miles:
      
    ```sql
    SELECT
        COUNT(*)
    FROM
        public.green_taxi_data
    WHERE
        lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
        AND trip_distance > 10;
    ```


## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance?
Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance. 

- [ ] 2019-10-11
- [ ] 2019-10-24
- [ ] 2019-10-26
- [X] 2019-10-31

### Solution:
```sql
SELECT
    "PULocationID",
    SUM("total_amount") AS total_amount
FROM
    public.green_taxi_data
WHERE
    DATE("lpep_pickup_datetime") = '2019-10-18'
GROUP BY
    "PULocationID"
HAVING
    SUM("total_amount") > 13000
ORDER BY
    total_amount DESC
LIMIT 3;
```

## Question 5. Three biggest pickup zones

Which were the top pickup locations with over 13,000 in
`total_amount` (across all trips) for 2019-10-18?

Consider only `lpep_pickup_datetime` when filtering by date.
 
- [X] East Harlem North, East Harlem South, Morningside Heights
- [ ] East Harlem North, Morningside Heights
- [ ] Morningside Heights, Astoria Park, East Harlem South
- [ ] Bedford, East Harlem North, Astoria Park

### Solution:

```sql
SELECT
    "PULocationID",
    SUM("total_amount") AS total_amount
FROM
    public.green_taxi_data
WHERE
    DATE("lpep_pickup_datetime") = '2019-10-18'
GROUP BY
    "PULocationID"
HAVING
    SUM("total_amount") > 13000
ORDER BY
    total_amount DESC
LIMIT 3;
```

## Question 6. Largest tip

For the passengers picked up in October 2019 in the zone
named "East Harlem North" which was the drop off zone that had
the largest tip?

Note: it's `tip` , not `trip`

We need the name of the zone, not the ID.

- [ ] Yorkville West
- [X] JFK Airport
- [ ] East Harlem North
- [ ] East Harlem South

### Solution:

```sql
SELECT
    tz_dropoff."Zone" AS dropoff_zone,
    MAX(gt."tip_amount") AS largest_tip
FROM
    green_taxi_data gt
JOIN
    taxi_zones tz_pickup ON gt."PULocationID" = tz_pickup."LocationID"
JOIN
    taxi_zones tz_dropoff ON gt."DOLocationID" = tz_dropoff."LocationID"
WHERE
    tz_pickup."Zone" = 'East Harlem North'
    AND gt."lpep_pickup_datetime" >= '2019-10-01'
    AND gt."lpep_pickup_datetime" < '2019-11-01'
GROUP BY
    tz_dropoff."Zone"
ORDER BY
    largest_tip DESC
LIMIT 1;
```

## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](../../../01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Terraform Workflow

Which of the following sequences, **respectively**, describes the workflow for: 
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`

Answers:
- [ ] terraform import, terraform apply -y, terraform destroy
- [ ] teraform init, terraform plan -auto-apply, terraform rm
- [ ] terraform init, terraform run -auto-approve, terraform destroy
- [X] terraform init, terraform apply -auto-approve, terraform destroy
- [ ] terraform import, terraform apply -y, terraform rm


## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1
