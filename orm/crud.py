from sqlalchemy.orm import sessionmaker, joinedload
from models import engine, Student, Department, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

# Read students in Computer Science
students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for s in students:
    print(s.first_name, s.last_name)

# Read enrollments
enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        e.course.course_name
    )

print("CRUD completed successfully.")