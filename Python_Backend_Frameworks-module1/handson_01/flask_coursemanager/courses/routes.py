from flask import Blueprint, jsonify, request
from app import db
from courses.models import Course, Student

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json(
        [course.to_dict() for course in courses],
        200
    )


@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request must be JSON"}), 400

    required_fields = [
        "name",
        "code",
        "credits",
        "department_id"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(course.to_dict(), 201)


@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)

    data = request.get_json()

    if "name" in data:
        course.name = data["name"]

    if "code" in data:
        course.code = data["code"]

    if "credits" in data:
        course.credits = data["credits"]

    if "department_id" in data:
        course.department_id = data["department_id"]

    db.session.commit()

    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return make_response_json(
        {"message": "Course deleted"},
        200
    )


@courses_bp.route("/<int:course_id>/students/", methods=["GET"])
def get_course_students(course_id):
    course = Course.query.get_or_404(course_id)

    students = [
        enrollment.student.to_dict()
        for enrollment in course.enrollments
    ]

    return make_response_json(students, 200)