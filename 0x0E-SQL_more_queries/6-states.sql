-- Creates a hbtn_0d_usa database and use it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Creates states table
CREATE TABLE IF NOT EXISTS states(
       id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
       name VARCHAR(256)
);
