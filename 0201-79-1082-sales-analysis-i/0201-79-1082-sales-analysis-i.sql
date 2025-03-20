SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
   SELECT SUM(price) as pricing
   FROM Sales
   GROUP BY seller_id
   ORDER BY pricing DESC
   LIMIT 1
)