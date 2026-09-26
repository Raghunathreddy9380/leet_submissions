SELECT MAX(salary) as secondhighestsalary
From Employee
Where salary<(SELECT MAX(salary)From Employee);