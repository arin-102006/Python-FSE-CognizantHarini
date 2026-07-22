from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_engine(
    "mysql+mysqlconnector://root:DAMPHubbub,102006@localhost/college_db",
    echo=True
)

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100))
    head_of_dept = Column(String(100))
    budget = Column(Numeric(12,2))

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)

    department = relationship("Department")

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(150))
    course_code = Column(String(20))
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student")
    course = relationship("Course")

class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    prof_name = Column(String(100))
    email = Column(String(100))
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10,2))

Base.metadata.create_all(engine)

print("Tables created successfully.")