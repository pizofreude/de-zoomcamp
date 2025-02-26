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