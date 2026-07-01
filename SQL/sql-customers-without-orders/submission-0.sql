-- Write your query below
SELECT c.name as name
FROM customers as c
LEFT JOIN orders as o
ON c.id = o.customer_id
where o.customer_id IS NULL;

