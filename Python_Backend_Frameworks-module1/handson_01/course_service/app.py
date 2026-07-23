from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "courses.db"


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.json

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO courses(name, department) VALUES(?, ?)",
        (data["name"], data["department"])
    )

    conn.commit()
    course_id = cur.lastrowid
    conn.close()

    return jsonify({
        "id": course_id,
        "message": "Course added successfully"
    }), 201


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT id,name,department FROM courses WHERE id=?",
        (id,)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "department": row[2]
        })

    return jsonify({"error": "Course not found"}), 404


if __name__ == "__main__":
    init_db()
    app.run(port=5001, debug=True)