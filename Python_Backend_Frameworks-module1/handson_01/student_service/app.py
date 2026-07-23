from flask import Flask, request, jsonify
import sqlite3
import requests
from requests.exceptions import ConnectionError

app = Flask(__name__)
DB = "students.db"


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students(name) VALUES(?)",
        (data["name"],)
    )

    conn.commit()
    student_id = cur.lastrowid
    conn.close()

    return jsonify({
        "id": student_id,
        "message": "Student added successfully"
    }), 201


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):
    data = request.json
    course_id = data["course_id"]

    try:
        response = requests.get(f"http://127.0.0.1:5001/api/courses/{course_id}")

        if response.status_code != 200:
            return jsonify({"error": "Course not found"}), 404

    except ConnectionError:
        return jsonify({
            "error": "Course Service unavailable"
        }), 503

    return jsonify({
        "message": f"Student {id} enrolled in course {course_id}"
    })


if __name__ == "__main__":
    init_db()
    app.run(port=5002, debug=True)