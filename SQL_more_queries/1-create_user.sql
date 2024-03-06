-- Attempt to create the user and set the password, ignore errors if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;
