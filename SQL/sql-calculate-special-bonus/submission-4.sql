-- Write your query below

SELECT employee_id,
       salary * 1 AS bonus
FROM employees
WHERE employee_id % 2 != 0
  AND name NOT LIKE '%M';