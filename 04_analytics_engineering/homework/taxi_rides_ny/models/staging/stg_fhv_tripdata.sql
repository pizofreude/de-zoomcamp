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