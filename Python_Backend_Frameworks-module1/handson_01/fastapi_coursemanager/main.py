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
from sqlalchemy import select, func, or_

from database import get_db, engine
from models import Base, Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    PaginatedCourses,
)

# API Versioning:
# URL Versioning: /api/v1/
# Alternative: Header Versioning using
# Accept: application/vnd.api+json;version=1

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API following REST Best Practices",
    version="2.1",
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


def error_response(code: str, message: str, field=None):
    raise HTTPException(
        status_code=404 if code == "NOT_FOUND" else 400,
        detail={
            "error": {
                "code": code,
                "message": message,
                "field": field,
            }
        },
    )


@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    obj = Course(**course.model_dump())

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    response.headers["Location"] = f"/api/v1/courses/{obj.id}/"

    return obj


@app.get(
    "/api/v1/courses/",
    response_model=PaginatedCourses,
)
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Course)

    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%"),
            )
        )

    total = await db.scalar(
        select(func.count()).select_from(query.subquery())
    )

    result = await db.execute(
        query.offset((page - 1) * page_size).limit(page_size)
    )

    courses = result.scalars().all()

    next_page = (
        f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        if page * page_size < total
        else None
    )

    previous_page = (
        f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        if page > 1
        else None
    )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": courses,
    }


@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
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
        error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist",
        )

    return course
@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
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
        error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist",
        )

    obj.name = course.name
    obj.code = course.code
    obj.credits = course.credits
    obj.department_id = course.department_id

    await db.commit()
    await db.refresh(obj)

    return obj


@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    obj = result.scalar_one_or_none()

    if obj is None:
        error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist",
        )

    updates = course.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(obj, key, value)

    await db.commit()
    await db.refresh(obj)

    return obj


@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
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
        error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist",
        )

    await db.delete(obj)
    await db.commit()

    return Response(status_code=204)


@app.post(
    "/api/v1/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    obj = Student(**student.model_dump())

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    response.headers["Location"] = f"/api/v1/students/{obj.id}/"

    return obj


@app.get("/api/v1/courses/{course_id}/students/")
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student)
        .join(
            Enrollment,
            Student.id == Enrollment.student_id,
        )
        .where(
            Enrollment.course_id == course_id
        )
    )

    return result.scalars().all()


@app.post(
    "/api/v1/enrollments/",
    status_code=status.HTTP_201_CREATED,
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    obj = Enrollment(**enrollment.model_dump())

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    response.headers["Location"] = (
        f"/api/v1/enrollments/{obj.id}/"
    )

    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com",
    )

    return {
        "message": "Enrollment created"
    }