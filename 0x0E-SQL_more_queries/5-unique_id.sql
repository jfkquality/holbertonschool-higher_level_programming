-- creates the table unique_id on your MySQL server.
-- unique_id description:
-- id INT DEFAULT 1 UNIQUE
-- name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
