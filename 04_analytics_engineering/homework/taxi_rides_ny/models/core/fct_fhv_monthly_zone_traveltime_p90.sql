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