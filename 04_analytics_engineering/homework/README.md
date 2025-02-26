## Module 4 Homework

For this homework, you will need the following datasets:
* [Green Taxi dataset (2019 and 2020)](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green)
* [Yellow Taxi dataset (2019 and 2020)](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow)
* [For Hire Vehicle dataset (2019)](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv)

> **Note**:
> 1. Update `docker-compose.yml` to include metabase container and run docker-compose up
> 2. Ingest specified Green Taxi, Yellow Taxi, FHV datasets into postgres container via kestra workflow (see `flows/02_postgres_taxi_fhv_scheduled.yaml`)
> 

### Before you start

1. Make sure you, **at least**, have them in GCS with a External Table **OR** a Native Table - use whichever method you prefer to accomplish that (Workflow Orchestration with [pandas-gbq](https://cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-to-gbq-simple), [dlt for gcs](https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem), [dlt for BigQuery](https://dlthub.com/docs/dlt-ecosystem/destinations/bigquery), [gsutil](https://cloud.google.com/storage/docs/gsutil), etc)
2. You should have exactly `7,778,101` records in your Green Taxi table
3. You should have exactly `109,047,518` records in your Yellow Taxi table
4. You should have exactly `43,244,696` records in your FHV table
5. Build the staging models for green/yellow as shown in [here](taxi_rides_ny/models/staging/)
6. Build the dimension/fact for taxi_trips joining with `dim_zones`  as shown in [here](taxi_rides_ny/models/core/fact_trips.sql)

**Note**: If you don't have access to GCP, you can spin up a local Postgres instance and ingest the datasets above


### Question 1: Understanding dbt model resolution

Provided you've got the following sources.yaml
```yaml
version: 2

sources:
  - name: raw_nyc_tripdata
    database: "{{ env_var('DBT_BIGQUERY_PROJECT', 'dtc_zoomcamp_2025') }}"
    schema:   "{{ env_var('DBT_BIGQUERY_SOURCE_DATASET', 'raw_nyc_tripdata') }}"
    tables:
      - name: ext_green_taxi
      - name: ext_yellow_taxi
```

with the following env variables setup where `dbt` runs:
```shell
export DBT_BIGQUERY_PROJECT=myproject
export DBT_BIGQUERY_DATASET=my_nyc_tripdata
```

What does this .sql model compile to?
```sql
select * 
from {{ source('raw_nyc_tripdata', 'ext_green_taxi' ) }}
```

- [ ] `select * from dtc_zoomcamp_2025.raw_nyc_tripdata.ext_green_taxi`
- [ ] `select * from dtc_zoomcamp_2025.my_nyc_tripdata.ext_green_taxi`
- [ ] `select * from myproject.raw_nyc_tripdata.ext_green_taxi`
- [X] `select * from myproject.my_nyc_tripdata.ext_green_taxi`
- [ ] `select * from dtc_zoomcamp_2025.raw_nyc_tripdata.green_taxi`


### Question 2: dbt Variables & Dynamic Models

Say you have to modify the following dbt_model (`fct_recent_taxi_trips.sql`) to enable Analytics Engineers to dynamically control the date range. 

- In development, you want to process only **the last 7 days of trips**
- In production, you need to process **the last 30 days** for analytics

```sql
select *
from {{ ref('fact_taxi_trips') }}
where pickup_datetime >= CURRENT_DATE - INTERVAL '30' DAY
```

What would you change to accomplish that in a such way that command line arguments takes precedence over ENV_VARs, which takes precedence over DEFAULT value?

- [ ] Add `ORDER BY pickup_datetime DESC` and `LIMIT {{ var("days_back", 30) }}`
- [ ] Update the WHERE clause to `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", 30) }}' DAY`
- [ ] Update the WHERE clause to `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ env_var("DAYS_BACK", "30") }}' DAY`
- [X] Update the WHERE clause to `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY`
- [ ] Update the WHERE clause to `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ env_var("DAYS_BACK", var("days_back", "30")) }}' DAY`

### Solutions:
To enable Analytics Engineers to dynamically control the date range, we should update the WHERE clause to use `var` with a fallback to `env_var`. This way, command line arguments take precedence over environment variables, which in turn take precedence over a default value.

```sql
select *
from {{ ref('fact_taxi_trips') }}
where pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY
```

Explanation:
- Command Line Arguments: var("days_back", ...) allows us to specify the days_back variable at runtime using the --vars option in the dbt command.
- Environment Variables: env_var("DAYS_BACK", ...) allows us to set the DAYS_BACK environment variable to override the default value.
- Default Value: "30" is the default value that will be used if neither a command line argument nor an environment variable is provided.


### Question 3: dbt Data Lineage and Execution

Considering the data lineage below **and** that taxi_zone_lookup is the **only** materialization build (from a .csv seed file):

![image](./homework_q2.png)

Select the option that does **NOT** apply for materializing `fct_taxi_monthly_zone_revenue`:

- [ ] `dbt run`
- [ ] `dbt run --select +models/core/dim_taxi_trips.sql+ --target prod`
- [ ] `dbt run --select +models/core/fct_taxi_monthly_zone_revenue.sql`
- [ ] `dbt run --select +models/core/`
- [X] `dbt run --select models/staging/+`
  
### Solution:
> Because it excludes `dim_zones.sql` which is a dependency of `fct_taxi_monthly_zone_revenue.sql`


### Question 4: dbt Macros and Jinja

Consider you're dealing with sensitive data (e.g.: [PII](https://en.wikipedia.org/wiki/Personal_data)), that is **only available to your team and very selected few individuals**, in the `raw layer` of your DWH (e.g: a specific BigQuery dataset or PostgreSQL schema), 

 - Among other things, you decide to obfuscate/masquerade that data through your staging models, and make it available in a different schema (a `staging layer`) for other Data/Analytics Engineers to explore

- And **optionally**, yet  another layer (`service layer`), where you'll build your dimension (`dim_`) and fact (`fct_`) tables (assuming the [Star Schema dimensional modeling](https://www.databricks.com/glossary/star-schema)) for Dashboarding and for Tech Product Owners/Managers

You decide to make a macro to wrap a logic around it:

```sql
{% macro resolve_schema_for(model_type) -%}

    {%- set target_env_var = 'DBT_BIGQUERY_TARGET_DATASET'  -%}
    {%- set stging_env_var = 'DBT_BIGQUERY_STAGING_DATASET' -%}

    {%- if model_type == 'core' -%} {{- env_var(target_env_var) -}}
    {%- else -%}                    {{- env_var(stging_env_var, env_var(target_env_var)) -}}
    {%- endif -%}

{%- endmacro %}
```

And use on your staging, dim_ and fact_ models as:
```sql
{{ config(
    schema=resolve_schema_for('core'), 
) }}
```

That all being said, regarding macro above, **select all statements that are true to the models using it**:
- [X] Setting a value for  `DBT_BIGQUERY_TARGET_DATASET` env var is mandatory, or it'll fail to compile
- [ ] Setting a value for `DBT_BIGQUERY_STAGING_DATASET` env var is mandatory, or it'll fail to compile
- [X] When using `core`, it materializes in the dataset defined in `DBT_BIGQUERY_TARGET_DATASET`
- [X] When using `stg`, it materializes in the dataset defined in `DBT_BIGQUERY_STAGING_DATASET`, or defaults to `DBT_BIGQUERY_TARGET_DATASET`
- [X] When using `staging`, it materializes in the dataset defined in `DBT_BIGQUERY_STAGING_DATASET`, or defaults to `DBT_BIGQUERY_TARGET_DATASET`

### Solution:
Only the second statement is wrong since the `DBT_BIGQUERY_STAGING_DATASET` environment variable is optional because the macro falls back to `DBT_BIGQUERY_TARGET_DATASET` if `DBT_BIGQUERY_STAGING_DATASET` is not set.

## Serious SQL

Alright, in module 1, you had a SQL refresher, so now let's build on top of that with some serious SQL.

These are not meant to be easy - but they'll boost your SQL and Analytics skills to the next level.  
So, without any further do, let's get started...

You might want to add some new dimensions `year` (e.g.: 2019, 2020), `quarter` (1, 2, 3, 4), `year_quarter` (e.g.: `2019/Q1`, `2019-Q2`), and `month` (e.g.: 1, 2, ..., 12), **extracted from pickup_datetime**, to your `fct_taxi_trips` OR `dim_taxi_trips.sql` models to facilitate filtering your queries


### Question 5: Taxi Quarterly Revenue Growth

1. Create a new model `fct_taxi_trips_quarterly_revenue.sql`
2. Compute the Quarterly Revenues for each year for based on `total_amount`
3. Compute the Quarterly YoY (Year-over-Year) revenue growth 
  * e.g.: In 2020/Q1, Green Taxi had -12.34% revenue growth compared to 2019/Q1
  * e.g.: In 2020/Q4, Yellow Taxi had +34.56% revenue growth compared to 2019/Q4

Considering the YoY Growth in 2020, which were the yearly quarters with the best (or less worse) and worst results for green, and yellow

- [ ] green: {best: 2020/Q2, worst: 2020/Q1}, yellow: {best: 2020/Q2, worst: 2020/Q1}
- [ ] green: {best: 2020/Q2, worst: 2020/Q1}, yellow: {best: 2020/Q3, worst: 2020/Q4}
- [ ] green: {best: 2020/Q1, worst: 2020/Q2}, yellow: {best: 2020/Q2, worst: 2020/Q1}
- [X] green: {best: 2020/Q1, worst: 2020/Q2}, yellow: {best: 2020/Q1, worst: 2020/Q2}
- [ ] green: {best: 2020/Q1, worst: 2020/Q2}, yellow: {best: 2020/Q3, worst: 2020/Q4}

### Solution:

We create the following files to implement the solution:

1. [fct_taxi_trips_quarterly_revenue.sql](taxi_rides_ny/models/core/fct_taxi_trips_quarterly_revenue.sql) - This model will compute the quarterly revenues and the YoY growth.
2. [analyze_quarterly_growth.sql](taxi_rides_ny/models/core/analyze_quarterly_growth.sql) - This query will analyze the results and identify the best and worst quarters.

#### 1. `fct_taxi_trips_quarterly_revenue.sql`

```sql name=models/core/fct_taxi_trips_quarterly_revenue.sql
{{
    config(
        materialized='table'
    )
}}

-- Step 1: Extract the year, quarter, and service type from pickup_datetime
with temp as (
    SELECT 
        EXTRACT(YEAR FROM pickup_datetime) AS year, 
        EXTRACT(QUARTER FROM pickup_datetime) AS quarter, 
        service_type, 
        total_amount
    FROM {{ ref('fact_trips') }}
),

-- Step 2: Group by service_type, year, and quarter to calculate total quarterly revenue
grouped as (
    SELECT 
        service_type, 
        year, 
        quarter, 
        SUM(total_amount) AS total_amount 
    FROM temp
    GROUP BY service_type, year, quarter
)

-- Step 3: Calculate YoY percentage change for each quarter
SELECT 
    service_type,
    year,
    quarter,
    total_amount,
    -- Get the total amount for the same quarter in the previous year
    LAG(total_amount) OVER (
        PARTITION BY service_type, quarter ORDER BY year
    ) AS prev_year_total_amount,
    -- Calculate YoY percentage change, avoid division by zero
    CASE 
        WHEN LAG(total_amount) OVER (
            PARTITION BY service_type, quarter ORDER BY year
        ) = 0 THEN NULL
        ELSE ROUND(
            (total_amount - LAG(total_amount) OVER (
                PARTITION BY service_type, quarter ORDER BY year
            )) / NULLIF(LAG(total_amount) OVER (
                PARTITION BY service_type, quarter ORDER BY year
            ), 0) * 100, 2
        )
    END AS yoy_percentage_change
FROM grouped
ORDER BY service_type, year, quarter;
```

#### 2. `analyze_quarterly_growth.sql`

```sql name=models/analyze_quarterly_growth.sql
-- Step 1: Filter results for the year 2020 and format year_quarter
with quarterly_growth as (
    SELECT
        service_type,
        year,
        CONCAT(year, '/Q', quarter) AS year_quarter,
        yoy_percentage_change
    FROM {{ ref('fct_taxi_trips_quarterly_revenue') }}
    WHERE year = 2020
)

-- Step 2: Select and order results by YoY percentage change
SELECT
    service_type,
    year_quarter,
    yoy_percentage_change
FROM quarterly_growth
ORDER BY service_type, yoy_percentage_change DESC;
```

### Summary

1. **Extract Year and Quarter**: We first extract the year and quarter from the `pickup_datetime` and calculate the total amount for each service type.
2. **Group by Year and Quarter**: We group the data by service type, year, and quarter to calculate the total quarterly revenue.
3. **Calculate YoY Growth**: We calculate the Year-over-Year percentage change for each quarter, using the `LAG` function to get the revenue for the same quarter in the previous year.
4. **Analyze Results**: We filter the results for the year 2020 and order them by YoY percentage change to identify the best and worst quarters.


### Question 6: P97/P95/P90 Taxi Monthly Fare

1. Create a new model `fct_taxi_trips_monthly_fare_p95.sql`
2. Filter out invalid entries (`fare_amount > 0`, `trip_distance > 0`, and `payment_type_description in ('Cash', 'Credit Card')`)
3. Compute the **continous percentile** of `fare_amount` partitioning by service_type, year and and month

Now, what are the values of `p97`, `p95`, `p90` for Green Taxi and Yellow Taxi, in April 2020?

- [ ] green: {p97: 55.0, p95: 45.0, p90: 26.5}, yellow: {p97: 52.0, p95: 37.0, p90: 25.5}
- [X] green: {p97: 55.0, p95: 45.0, p90: 26.5}, yellow: {p97: 31.5, p95: 25.5, p90: 19.0}
- [ ] green: {p97: 40.0, p95: 33.0, p90: 24.5}, yellow: {p97: 52.0, p95: 37.0, p90: 25.5}
- [ ] green: {p97: 40.0, p95: 33.0, p90: 24.5}, yellow: {p97: 31.5, p95: 25.5, p90: 19.0}
- [ ] green: {p97: 55.0, p95: 45.0, p90: 26.5}, yellow: {p97: 52.0, p95: 25.5, p90: 19.0}

### Solution:

### Steps 1

**Create a new model [fct_taxi_trips_monthly_fare_p95.sql](taxi_rides_ny/models/core/fct_taxi_trips_monthly_fare_p95.sql):**
   - This model will filter out invalid entries.
   - Compute the continuous percentiles (P97, P95, P90) of `fare_amount` partitioned by `service_type`, `year`, and `month`.


We first filter out the invalid entries and then calculate the continuous percentiles for the `fare_amount`.

```sql name=models/core/fct_taxi_trips_monthly_fare_p95.sql
{{
    config(
        materialized='table'
    )
}}

-- Step 1: Filter out invalid entries
with valid_trips as (
    SELECT 
        service_type, 
        EXTRACT(YEAR FROM pickup_datetime) AS year, 
        EXTRACT(MONTH FROM pickup_datetime) AS month, 
        fare_amount
    FROM {{ ref('fact_trips') }}
    WHERE fare_amount > 0 
      AND trip_distance > 0 
      AND payment_type_description IN ('Cash', 'Credit Card')
),

-- Step 2: Compute continuous percentiles (P97, P95, P90)
percentiles as (
    SELECT 
        service_type,
        year,
        month,
        APPROX_QUANTILES(fare_amount, 100)[OFFSET(97)] AS p97,
        APPROX_QUANTILES(fare_amount, 100)[OFFSET(95)] AS p95,
        APPROX_QUANTILES(fare_amount, 100)[OFFSET(90)] AS p90
    FROM valid_trips
    GROUP BY service_type, year, month
)

SELECT
    service_type,
    year,
    month,
    p97,
    p95,
    p90
FROM percentiles
ORDER BY service_type, year, month;
```

### Analysis Query

To analyze the values for Green Taxi and Yellow Taxi in April 2020, we filter the results via [analyze_monthly_percentiles.sql](taxi_rides_ny/models/core/analyze_monthly_percentiles.sql)

```sql name=models/core/analyze_monthly_percentiles.sql
-- Step 1: Filter results for April 2020
with monthly_percentiles as (
    SELECT
        service_type,
        year,
        month,
        p97,
        p95,
        p90
    FROM {{ ref('fct_taxi_trips_monthly_fare_p95') }}
    WHERE year = 2020 AND month = 4
)

-- Step 2: Select and order results
SELECT
    service_type,
    p97,
    p95,
    p90
FROM monthly_percentiles
ORDER BY service_type;
```

### Summary of Results

By running the above query, we get the continuous percentiles for April 2020 for both Green and Yellow taxis:

- **Green Taxi:**
  - P97: 55.0
  - P95: 45.0
  - P90: 26.5

- **Yellow Taxi:**
  - P97: 31.5
  - P95: 25.5
  - P90: 19.0


### Question 7: Top #Nth longest P90 travel time Location for FHV

Prerequisites:
* Create a staging model for FHV Data (2019), and **DO NOT** add a deduplication step, just filter out the entries where `where dispatching_base_num is not null`
* Create a core model for FHV Data (`dim_fhv_trips.sql`) joining with `dim_zones`. Similar to what has been done [here](taxi_rides_ny/models/core/fact_trips.sql)
* Add some new dimensions `year` (e.g.: 2019) and `month` (e.g.: 1, 2, ..., 12), based on `pickup_datetime`, to the core model to facilitate filtering for your queries

Now...
1. Create a new model `fct_fhv_monthly_zone_traveltime_p90.sql`
2. For each record in `dim_fhv_trips.sql`, compute the [timestamp_diff](https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_diff) in seconds between dropoff_datetime and pickup_datetime - we'll call it `trip_duration` for this exercise
3. Compute the **continous** `p90` of `trip_duration` partitioning by year, month, pickup_location_id, and dropoff_location_id

For the Trips that **respectively** started from `Newark Airport`, `SoHo`, and `Yorkville East`, in November 2019, what are **dropoff_zones** with the 2nd longest p90 trip_duration ?

- [X] LaGuardia Airport, Chinatown, Garment District
- [ ] LaGuardia Airport, Park Slope, Clinton East
- [ ] LaGuardia Airport, Saint Albans, Howard Beach
- [ ] LaGuardia Airport, Rosedale, Bath Beach
- [ ] LaGuardia Airport, Yorkville East, Greenpoint

### Solution:

We create the following files to implement the solution:

1. [stg_fhv_tripdata.sql](taxi_rides_ny/models/staging/stg_fhv_tripdata.sql) - Staging model for FHV Data (2019).
2. [dim_fhv_trips.sql](taxi_rides_ny/models/core/dim_fhv_trips.sql) - Core model for FHV Data.
3. [fct_fhv_monthly_zone_traveltime_p90.sql](taxi_rides_ny/models/core/fct_fhv_monthly_zone_traveltime_p90.sql) - Fact model to compute p90 trip_duration.
4. [analyze_longest_p90_travel_time.sql](taxi_rides_ny/models/core/analyze_longest_p90_travel_time.sql) - Analysis query to find the 2nd longest p90 trip_duration for specified pickup locations.

#### 1. Staging Model for FHV Data (2019): [stg_fhv_tripdata.sql](taxi_rides_ny/models/staging/stg_fhv_tripdata.sql)

```sql name=models/staging/stg_fhv_tripdata.sql
{{ config(materialized='view') }}

with tripdata as (
  select *
  from {{ source('staging', 'fhv_tripdata') }}
  where Dispatching_base_num is not null
)
select
    unique_row_id,
    Dispatching_base_num,
    cast(Pickup_datetime as timestamp) as pickup_datetime,
    cast(DropOff_datetime as timestamp) as dropoff_datetime,
    {{ dbt.safe_cast("PULocationID", api.Column.translate_type("integer")) }} as pickup_locationid,
    {{ dbt.safe_cast("DOLocationID", api.Column.translate_type("integer")) }} as dropoff_locationid,
    SR_Flag
from tripdata
```

#### 2. Core Model for FHV Data: [dim_fhv_trips.sql](taxi_rides_ny/models/core/dim_fhv_trips.sql)

```sql name=models/core/dim_fhv_trips.sql
{{
    config(
        materialized='table'
    )
}}

with tripdata as (
    select *
    from {{ ref('stg_fhv_tripdata') }}
), 
dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)
select
    tripdata.unique_row_id,
    tripdata.Dispatching_base_num,
    tripdata.pickup_datetime,
    tripdata.dropoff_datetime,
    tripdata.pickup_locationid,
    tripdata.dropoff_locationid,
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone,
    tripdata.SR_Flag,
    EXTRACT(YEAR FROM pickup_datetime) AS year, 
    EXTRACT(MONTH FROM pickup_datetime) AS month
from tripdata
inner join dim_zones as pickup_zone
on tripdata.pickup_locationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on tripdata.dropoff_locationid = dropoff_zone.locationid
```

#### 3. Fact Model to Compute p90 Trip Duration: [fct_fhv_monthly_zone_traveltime_p90.sql](taxi_rides_ny/models/core/fct_fhv_monthly_zone_traveltime_p90.sql)

```sql name=models/core/fct_fhv_monthly_zone_traveltime_p90.sql
{{
    config(
        materialized='view'
    )
}}

with temp as (
    select
        unique_row_id,
        Dispatching_base_num,
        pickup_locationid,
        dropoff_locationid,
        pickup_datetime,
        dropoff_datetime,
        TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, SECOND) as trip_duration,
        pickup_zone,
        dropoff_zone,
        year,
        month
    from {{ ref('dim_fhv_trips') }}
    where pickup_zone in ('Newark Airport', 'SoHo', 'Yorkville East') and year = 2019 and month = 11
)
select 
    year, 
    month,
    pickup_locationid,
    dropoff_locationid,
    pickup_zone,
    dropoff_zone,
    PERCENTILE_CONT(trip_duration, 0.90) OVER (PARTITION BY year, month, pickup_locationid, dropoff_locationid) as p90
from temp
order by
    pickup_zone, p90 desc
```

#### 4. Analysis Query: [analyze_longest_p90_travel_time.sql](taxi_rides_ny/models/core/analyze_longest_p90_travel_time.sql)

```sql name=models/core/analyze_longest_p90_travel_time.sql
-- Step 1: Filter results for November 2019
with november_2019 as (
    select
        pickup_zone,
        dropoff_zone,
        p90,
        ROW_NUMBER() OVER (PARTITION BY pickup_zone ORDER BY p90 DESC) as rn
    from {{ ref('fct_fhv_monthly_zone_traveltime_p90') }}
    where year = 2019 and month = 11
)

-- Step 2: Select the 2nd longest p90 trip duration for each specified pickup zone
select
    pickup_zone,
    dropoff_zone,
    p90
from november_2019
where rn = 2
order by pickup_zone;
```


### Summary of Results Q7

By running the above queries, we get the dropoff zones with the 2nd longest p90 trip_duration for trips starting from `Newark Airport`, `SoHo`, and `Yorkville East` in November 2019:

- **Newark Airport:** LaGuardia Airport
- **SoHo:** Chinatown
- **Yorkville East:** Garment District

## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw4


## Solution 

* To be published after deadline
