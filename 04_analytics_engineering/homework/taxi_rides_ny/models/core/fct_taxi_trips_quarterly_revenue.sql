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