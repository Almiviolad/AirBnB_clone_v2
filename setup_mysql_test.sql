-- my sql file to prepare for the project
-- create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates user on localhost with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all priviledge on database hbnb_test_db to user
GRANT ALL PRIVILEGES ON hbnb_test_db .* TO 'hbnb_test'@'localhost';
-- grant the SELECT privilege to the user hbnb_test on the performance_schema
GRANT SELECT ON performance_schema .* TO 'hbnb_test'@'localhost';
