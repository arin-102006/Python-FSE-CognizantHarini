import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DAMPHubbub,102006",
    database="college_db"
)

cursor = conn.cursor()

# Step 56
start = time.time()

query_count = 1
cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for row in enrollments:
    student_id = row[1]
    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (student_id,)
    )
    cursor.fetchone()
    query_count += 1

end = time.time()

print("Step 56")
print("Queries executed:", query_count)
print("Time:", end - start)

# Step 57
start = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

end = time.time()

print("\nStep 57")
print("Queries executed: 1")
print("Time:", end - start)

# Step 58
print("\nStep 58")
print("JOIN query is much more efficient than N+1 queries.")

# Step 59
print("\nStep 59")
print("For 10,000 enrollments, the N+1 approach executes about 10,001 queries.")
print("The JOIN approach executes only 1 query.")

cursor.close()
conn.close()