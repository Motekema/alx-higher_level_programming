-- 5-unique_id.sql

-- Create table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Insert data into unique_id
INSERT INTO unique_id (id, name) VALUES (89, 'Best School');

-- Query data from unique_id
SELECT * FROM unique_id;

