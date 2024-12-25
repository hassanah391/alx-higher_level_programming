-- Creates a database called hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates a users called user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Give user_0d_2 user only SELECT privilege in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
