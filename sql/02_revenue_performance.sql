SELECT order_date, product_id,
SUM(quantity*unit_price*(1-discount)) net_revenue
FROM orders WHERE status NOT IN ('Cancelled','Returned')
GROUP BY order_date,product_id;
