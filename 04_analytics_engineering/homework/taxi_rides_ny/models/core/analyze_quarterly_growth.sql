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