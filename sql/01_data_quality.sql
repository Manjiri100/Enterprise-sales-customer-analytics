-- Duplicate customers
SELECT customer_id, COUNT(*) records FROM customers GROUP BY customer_id HAVING COUNT(*)>1;
-- Invalid customer keys
SELECT COUNT(*) invalid_customer_keys FROM orders o LEFT JOIN customers c ON o.customer_id=c.customer_id WHERE c.customer_id IS NULL;
-- Invalid quantities and discounts
SELECT COUNT(*) invalid_orders FROM orders WHERE quantity<=0 OR discount<0 OR discount>1;
