-- Generate table with mandatory ID
-- Ensures 'id_not_null' table's creation on MySQL
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
-- Display MySQL users' rights
-- Enumerates 'user_0d_1' and 'user_0d_2' privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
