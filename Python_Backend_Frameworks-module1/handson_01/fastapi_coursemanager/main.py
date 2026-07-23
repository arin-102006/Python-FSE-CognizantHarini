from typing import Optional

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    BackgroundTasks,
    Response,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db, engine
from models import Base, Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
)

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API for Course Management",
    version="2.0",
    contact={
        "name": "Harini SG",
        "email": "harini@example.com",
    },
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "API running"}


def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Course created successfully",
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    obj = Course(**course.model_dump())

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    return obj


@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"],
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Course)

    if department_id is not None:
        query = query.where(Course.department_id == department_id)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
)
async def update_course(
    course_id: int,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    obj = result.scalar_one_or_none()

    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    obj.name = course.name
    obj.code = course.code
    obj.credits = course.credits
    obj.department_id = course.department_id

    await db.commit()
    await db.refresh(obj)

    return obj


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"],
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    obj = result.scalar_one_or_none()

    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    await db.delete(obj)
    await db.commit()

    return Response(status_code=204)


@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=201,
    tags=["Students"],
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    obj = Student(**student.model_dump())

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    return obj


@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Courses"],
)
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .where(Enrollment.course_id == course_id)
    )

    return result.scalars().all()


@app.post(
    "/api/enrollments/",
    status_code=201,
    tags=["Enrollments"],
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    obj = Enrollment(**enrollment.model_dump())

    db.add(obj)
    await db.commit()

    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com",
    )

    return {"message": "Enrollment created"}