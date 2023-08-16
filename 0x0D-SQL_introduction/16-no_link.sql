-- This script selects the 'score' and 'name' columns from 'second_table'
-- where the 'name' is not null, sorting by 'score' in descending order.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
