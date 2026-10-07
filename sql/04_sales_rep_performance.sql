SELECT rep_id,COUNT(*) orders,
SUM(quantity*unit_price*(1-discount)) revenue
FROM orders WHERE status NOT IN ('Cancelled','Returned') GROUP BY rep_id;
