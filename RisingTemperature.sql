/* Write your T-SQL query statement below */
SELECT  W.ID                                       
FROM Weather W
WHERE W.Temperature > (SELECT TOP 1 Temperature FROM Weather E 
                       WHERE W.RecordDate = DATEADD(day,1,E.RecordDate)   
                      ORDER BY RecordDate DESC )