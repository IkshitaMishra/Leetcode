/* Write your T-SQL query statement below */ (Duplicate Emails)

SELECT A.Email 
FROM(
SELECT DISTINCT Email, COUNT(Email) OVER(PARTITION BY Email) AS EmailCount
FROM Person
) A
WHERE EmailCount >1