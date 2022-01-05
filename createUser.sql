--
-- Create a database user for `test`
--
CREATE USER 'pyuser'@'localhost' IDENTIFIED BY 'pyassword';
GRANT ALL PRIVILEGES ON test . * TO 'pyuser'@'localhost';
FLUSH PRIVILEGES;