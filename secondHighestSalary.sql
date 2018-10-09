/* Write your T-SQL query statement below */ (SECOND HIGHEST)

SELECT ISNULL(
(SELECT TOP 1 SALARY AS SecondHighestSalary 
FROM EMPLOYEE
WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)
ORDER BY SecondHighestSalary DESC),NULL) AS SecondHighestSalary
