# Write your MySQL query statement below


select (
    select distinct salary 
    From employee
    order by salary desc 
    limit 1 offset 1
)
as secondhighestsalary;