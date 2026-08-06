
-- Lecture 09 - Views and Stored Procedures


USE STUDENTSSS;


-- VIEW -> saved SELECT query / virtual table

CREATE OR REPLACE VIEW STUDENTS_PASS AS
SELECT *
FROM STUDENTS
WHERE CGPA >= 7.5;


SELECT *
FROM STUDENTS_PASS;


-- View complex query ko simple bana sakta hai
-- aur selected data expose karne me useful hai



-- Stored Procedure


DELIMITER $$

CREATE PROCEDURE GET_STUDENT_BY_CGPA(
    IN CGPA_XYZ DECIMAL(3, 2)
)
BEGIN
    SELECT *
    FROM STUDENTS
    WHERE CGPA = CGPA_XYZ;
END $$

DELIMITER ;


CALL GET_STUDENT_BY_CGPA(9.50);


-- Procedure delete karni ho:
-- DROP PROCEDURE GET_STUDENT_BY_CGPA;
