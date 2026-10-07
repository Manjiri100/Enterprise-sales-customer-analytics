select customer_id,count(*) order_count,
sum(quantity*unit_price*(1-discount)) revenue,max(order_date) last_order_date
from {{ ref('stg_orders') }} where status not in ('Cancelled','Returned') group by customer_id
