-- Check if user_0d_1 already exists
SELECT User FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost' LIMIT 1;

-- If user_0d_1 doesn't exist, create it with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;