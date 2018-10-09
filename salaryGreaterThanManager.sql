/* Write your T-SQL query statement below */ (Salary greater than Manager)


SELECT E1.NAME AS Employee
FROM EMPLOYEE E1
WHERE E1.SALARY > ( SELECT SALARY FROM EMPLOYEE WHERE ID = E1.MANAGERID)