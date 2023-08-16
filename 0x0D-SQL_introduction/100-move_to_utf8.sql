-- This script alters the character set and collation of the 'first_table' to 'utf8mb4' and 'utf8mb4_unicode_ci' respectively
USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
