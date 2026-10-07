SELECT COUNT(*) raw_orders,
SUM(CASE WHEN quantity<=0 OR discount<0 OR discount>1 THEN 1 ELSE 0 END) anomalous_orders,
SUM(CASE WHEN status NOT IN ('Cancelled','Returned') THEN quantity*unit_price*(1-discount) ELSE 0 END) net_revenue
FROM orders;
