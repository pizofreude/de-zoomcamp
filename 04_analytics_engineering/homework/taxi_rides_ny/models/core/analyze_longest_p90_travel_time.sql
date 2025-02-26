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