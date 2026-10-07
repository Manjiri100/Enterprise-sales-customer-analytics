select count(*) order_records,
sum(case when quantity<=0 or discount<0 or discount>1 then 1 else 0 end) anomalous_orders
from {{ ref('stg_orders') }}
