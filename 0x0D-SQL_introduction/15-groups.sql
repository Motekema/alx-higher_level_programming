-- Script to list the number of records with the same score in second_table

-- Grouping records by score and counting the number of occurrences
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;

