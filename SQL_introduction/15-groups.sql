-- List the number of records by score, sorted by the count in descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
