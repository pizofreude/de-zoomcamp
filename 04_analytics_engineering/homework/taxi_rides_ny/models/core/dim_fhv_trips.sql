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