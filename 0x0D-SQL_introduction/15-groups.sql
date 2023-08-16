-- This script selects the score and number of occurrences from the 'second_table',
-- grouping by the score and ordering descending by number of occurrences
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
