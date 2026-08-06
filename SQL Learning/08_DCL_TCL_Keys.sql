-- Lecture 08 - DCL, TCL and SQL Keys


-- DCL -> database permissions


-- User create
CREATE USER 'testuser'@'localhost'
IDENTIFIED BY 'testpass';


-- Permissions
GRANT ALL PRIVILEGES
ON *.*
TO 'testuser'@'localhost';


-- Permissions remove
REVOKE ALL PRIVILEGES
ON *.*
FROM 'testuser'@'localhost';


-- Password change
ALTER USER 'testuser'@'localhost'
IDENTIFIED BY 'testpass1';


-- TCL - Transaction Control Language

USE STUDENTSSS;

START TRANSACTION;

INSERT INTO STUDENTS
VALUES (10, 'TEMP USER', 'JAIPUR', 7.5);

SAVEPOINT S1;

UPDATE STUDENTS
SET CGPA = 9.9
WHERE ID = 10;

ROLLBACK TO S1;

COMMIT;


-- Main Keys:
-- PRIMARY KEY   -> unique + not null
-- FOREIGN KEY   -> dusri table ki key reference
-- UNIQUE        -> duplicate values allowed nahi
-- Candidate Key -> primary key banne ke eligible columns
-- NOT NULL      -> value compulsory
-- DEFAULT       -> default value
-- CHECK         -> condition validate karta hai
-- INDEX         -> lookup/search performance improve karta hai
