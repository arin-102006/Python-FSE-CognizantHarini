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