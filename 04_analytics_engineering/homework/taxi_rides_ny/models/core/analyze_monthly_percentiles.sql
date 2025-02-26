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