-- Creates a id_not_null table
CREATE TABLE IF NOT EXISTS id_not_null(
id INT UNIQUE DEFAULT 1,
name VARCHAR(50)
);
