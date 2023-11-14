-- Script to list records with a score >= 10 in second_table

-- Selecting records from second_table with score >= 10 and ordering by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

