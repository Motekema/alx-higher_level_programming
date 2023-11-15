-- 3-force_name.sql

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert data into force_name
INSERT INTO force_name (id, name) VALUES (89, 'Best School');

-- Query data from force_name
SELECT * FROM force_name;

