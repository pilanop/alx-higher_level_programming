-- This script creates a table named 'second_table' if it doesn't already exist, then inserts four records into it.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES (id = 1, name = 'John', score = 10),
       (id = 2, name = 'Alex', score = 3),
       (id = 3, name = 'Bob', score = 14),
       (id = 4, name = 'George', score = 18)
