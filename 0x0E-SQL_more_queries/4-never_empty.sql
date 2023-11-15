-- 4-never_empty.sql

-- Create table id_not_null if it does not exist
-- Insert data into id_not_null
-- Query data from id_not_null
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
