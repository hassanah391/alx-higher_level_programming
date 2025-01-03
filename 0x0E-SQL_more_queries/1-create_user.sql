-- Creates a user called user_0d_1 with password user_0d_1_pwd
CREATE USER IF NOT EXISTS'user_0d_1'@'localhost' IDENTIFIED
BY 'user_0d_1_pwd';

-- Gives user_0d_1 user all privileges on your MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 3. Apply the changes
FLUSH PRIVILEGES;
