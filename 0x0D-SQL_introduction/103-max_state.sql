-- Script to import table dump and display the max temperature of each state

-- Import the table dump into hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/downloaded/table_dump.sql;

-- Display the max temperature of each state ordered by state name
SELECT state, MAX(temp_fahrenheit) as max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;

