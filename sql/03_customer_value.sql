SELECT customer_id,COUNT(*) orders,
SUM(quantity*unit_price*(1-discount)) revenue,MAX(order_date) last_order_date
FROM orders WHERE status NOT IN ('Cancelled','Returned') GROUP BY customer_id;
