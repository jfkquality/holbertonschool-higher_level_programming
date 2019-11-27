-- creates the table id_not_null on your MySQL server.
-- force_name description:
-- id INT not null. = 1
-- name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
