-- Script to import table dump and display top 3 cities' temperature during July and August

-- Import the table dump into hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE /path/to/your/downloaded/table_dump.sql;

-- Display the top 3 cities' temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temp_fahrenheit) as avg_temp
FROM temperature_data
WHERE month IN (7, 8) -- Assuming the month column is named 'month'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

