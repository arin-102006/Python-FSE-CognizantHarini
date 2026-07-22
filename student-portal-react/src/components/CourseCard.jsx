import { Link } from "react-router-dom";

function CourseCard({ course, onEnroll }) {
  return (
    <div className="course-card">
      <h2>{course.name}</h2>

      <p>{course.description}</p>

      <p>Credits: {course.credits}</p>

      <Link to={`/courses/${course.id}`}>
        <button>View Details</button>
      </Link>

      <button onClick={() => onEnroll(course)}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;