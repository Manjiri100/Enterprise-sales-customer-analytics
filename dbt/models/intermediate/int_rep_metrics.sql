select rep_id,count(*) order_count,
sum(quantity*unit_price*(1-discount)) revenue
from {{ ref('stg_orders') }} where status not in ('Cancelled','Returned') group by rep_id
