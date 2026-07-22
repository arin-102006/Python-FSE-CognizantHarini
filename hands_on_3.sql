-- Digital Nurture 5.0
-- Module 3: Database Integration
-- Hands-On 3
-- Name: Harini SG
-- Step 35
-- Find students who are enrolled in more courses than the average number of enrollments per student.

SELECT
    s.student_id,
    s.first_name,
    s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

SELECT
    c.course_id,
    c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
);
SELECT
    p.professor_id,
    p.first_name,
    p.last_name,
    p.department_id,
    p.salary
FROM professors p
WHERE p.salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);
SELECT *
FROM (
    SELECT department_id,
           AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 85000;
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.department_name,
    COUNT(e.course_id) AS total_courses,
    AVG(
        CASE
            WHEN e.grade='A' THEN 4
            WHEN e.grade='B' THEN 3
            WHEN e.grade='C' THEN 2
            WHEN e.grade='D' THEN 1
            ELSE 0
        END
    ) AS GPA
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY
s.student_id,
student_name,
d.department_name;
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    AVG(
        CASE
            WHEN e.grade='A' THEN 4
            WHEN e.grade='B' THEN 3
            WHEN e.grade='C' THEN 2
            WHEN e.grade='D' THEN 1
            ELSE 0
        END
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY
c.course_id,
c.course_name,
c.course_code;
SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3.0;
UPDATE vw_student_enrollment_summary
SET GPA=4
WHERE student_id=1;
DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
student_id,
first_name,
last_name,
department_id
FROM students
WHERE department_id IS NOT NULL
WITH CHECK OPTION;
DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
IN p_student_id INT,
IN p_course_id INT,
IN p_enrollment_date DATE
)
BEGIN

IF EXISTS(
SELECT *
FROM enrollments
WHERE student_id=p_student_id
AND course_id=p_course_id
)
THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT='Student already enrolled';

ELSE

INSERT INTO enrollments
(student_id,course_id,enrollment_date)
VALUES
(p_student_id,p_course_id,p_enrollment_date);

END IF;

END$$

DELIMITER ;
CREATE TABLE IF NOT EXISTS department_transfer_log(
log_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
IN p_student_id INT,
IN p_new_department INT
)
BEGIN

DECLARE old_dept INT;

START TRANSACTION;

SELECT department_id
INTO old_dept
FROM students
WHERE student_id=p_student_id;

UPDATE students
SET department_id=p_new_department
WHERE student_id=p_student_id;

INSERT INTO department_transfer_log
(student_id,old_department,new_department)
VALUES
(p_student_id,old_dept,p_new_department);

COMMIT;

END$$

DELIMITER ;
START TRANSACTION;

UPDATE students
SET department_id=999
WHERE student_id=1;

ROLLBACK;
START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)
VALUES
(1,2,CURDATE());

SAVEPOINT sp1;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)
VALUES
(1,999,CURDATE());

ROLLBACK TO sp1;

COMMIT;