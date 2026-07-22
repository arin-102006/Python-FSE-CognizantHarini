-- Digital Nurture 5.0
-- Module 3: Database Integration
-- Hands-On 4

-- Step 48
EXPLAIN FORMAT=JSON
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;
-- Step 49
-- Observation:
-- MySQL shows Full Table Scan if no suitable index exists.

-- Step 50
-- Observation:
-- Note the estimated rows examined from the EXPLAIN output.
-- Step 51
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);
-- Step 52
CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);
-- Step 53
CREATE INDEX idx_course_code
ON courses(course_code);
-- Step 54
EXPLAIN FORMAT=JSON
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id=e.student_id
JOIN courses c
ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;

-- Compare this plan with Step 48.
-- Step 55
-- PostgreSQL:
-- CREATE INDEX idx_null_grade
-- ON enrollments(student_id)
-- WHERE grade IS NULL;

-- MySQL does not support partial indexes.
