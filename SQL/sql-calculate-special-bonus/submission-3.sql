-- Write your query below

select employee_id,salary*1 as bonus from employees
where employee_id % 2 != 0 and name not like '%M';