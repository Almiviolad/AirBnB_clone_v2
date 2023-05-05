 -- prepare sql for project
 -- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user hbnb_dev with password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privilege tovuser
GRANT ALL PRIVILEGES ON hbnb_dev_db .* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema .* TO 'hbnb_dev'@'localhost';
