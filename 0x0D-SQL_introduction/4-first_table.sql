-- Script to create a table called first_table in the current database

-- Creating the first_table if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Displaying the tables in the current database
SHOW TABLES;

