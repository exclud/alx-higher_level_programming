-- Script to create MySQL server user user_0d_1.
-- This creates the user with all privillages
CREATE USER IF NOT EXISTS 'user_0d_1.'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- This grants the user all privillages
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES
