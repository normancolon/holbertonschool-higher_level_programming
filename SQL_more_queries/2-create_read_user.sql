-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Attempt to create the user and set the password, ignore errors if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the hbtn_0d_2 database only
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;
