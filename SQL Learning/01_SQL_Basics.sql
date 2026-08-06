
-- Lecture 01 - SQL Basics


-- SQL -> Structured Query Language
-- DBMS  -> database ko manage karta hai
-- RDBMS -> data tables ke form me store hota hai

-- Main SQL command types:
-- DDL -> CREATE, ALTER, DROP, TRUNCATE
-- DML -> INSERT, UPDATE, DELETE
-- DQL -> SELECT
-- DCL -> GRANT, REVOKE
-- TCL -> COMMIT, ROLLBACK, SAVEPOINT


CREATE DATABASE CSE;

SHOW DATABASES;

USE CSE;

SHOW TABLES;


-- Table create karna

CREATE TABLE CSE_STUDENTS (
    ROLL_NO INT PRIMARY KEY,
    FIRST_NAME VARCHAR(30),
    LAST_NAME VARCHAR(30),
    EMAIL VARCHAR(50),
    AGE INT
);

DESCRIBE CSE_STUDENTS;


-- Data insert

INSERT INTO CSE_STUDENTS
VALUES (1, 'Govind', 'Jangid', 'govind@gmail.com', 21);

INSERT INTO CSE_STUDENTS
VALUES
(2, 'Aman', 'Sharma', 'aman@gmail.com', 20),
(3, 'ASHI', 'Jain', 'riya@gmail.com', 21);



SELECT * FROM CSE_STUDENTS;


-- Dangerous commands khi sunna na pd jaye

-- DROP TABLE CSE_STUDENTS;
-- DROP DATABASE CSE;
