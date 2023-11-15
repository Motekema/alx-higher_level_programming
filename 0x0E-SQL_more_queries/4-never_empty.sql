-- 4-never_empty.sql

-- Create table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Insert data into id_not_null
INSERT INTO id_not_null (id, name) VALUES (89, 'Best School');

-- Query data from id_not_null
SELECT * FROM id_not_null;

