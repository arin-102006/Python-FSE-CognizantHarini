import { useSelector, useDispatch } from "react-redux";
import { removeCourse } from "../redux/enrollmentSlice";

import Header from "../components/Header";
import Footer from "../components/Footer";
import StudentProfile from "../components/StudentProfile";

function ProfilePage() {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  const dispatch = useDispatch();

  return (
    <>
      <Header />

      <StudentProfile />

      <h2>Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div
            key={course.id}
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              margin: "10px 0",
              borderRadius: "5px",
            }}
          >
            <h3>{course.name}</h3>
            <p>{course.description}</p>
            <p>Credits: {course.credits}</p>

            <button onClick={() => dispatch(removeCourse(course.id))}>
              Remove
            </button>
          </div>
        ))
      )}

      <Footer />
    </>
  );
}

export default ProfilePage;