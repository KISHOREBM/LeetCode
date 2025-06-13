select name as Employee  from Employee as E
where E.salary > (select salary from Employee where id = E.managerId);