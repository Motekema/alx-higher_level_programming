-- Script to convert hbtn_0c_0 database, first_table table, and name field to UTF8

-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to UTF8
ALTER TABLE first_table MODIFY COLUMN name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

