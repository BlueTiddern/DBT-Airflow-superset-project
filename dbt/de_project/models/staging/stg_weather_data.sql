{{config(
    materialized='table',
    unique_key='id'
)}}

WITH source as (
select *
FROM {{ source('dev', 'raw_weather') }}
),
de_dup as (

select
    *,
    row_number() over(partition by time order by inserted_at) as rn
from source

)

SELECT
    id,
    city,
    temperature,
    weather_description,
    wind_speed,
    time as weather_time_local,
    (inserted_at + (utc_offset || 'hours')::interval) as inserted_at_local
FROM de_dup
WHERE rn = 1