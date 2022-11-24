with source_store_sales as (
	select * from {{ source('source_snowflake', 'store_sales')  }}
),

final as (
	select * from source_store_sales
)

select * from final