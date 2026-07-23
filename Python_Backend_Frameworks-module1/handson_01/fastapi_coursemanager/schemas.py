from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    model_config = {"from_attributes": True}


class StudentCreate(BaseModel):
    name: str
    email: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {"from_attributes": True}


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: list[CourseResponse] = []

    model_config = {"from_attributes": True}


class ErrorDetail(BaseModel):
    code: str
    message: str
    field: Optional[str] = None


class ErrorResponse(BaseModel):
    error: ErrorDetail


class PaginatedCourses(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[CourseResponse]