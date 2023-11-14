-- Script to import table dump and display average temperature by city

-- Import the table dump into hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/downloaded/table_dump.sql;

-- Display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(temp_fahrenheit) as avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;

