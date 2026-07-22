import { useState, useEffect } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import CourseCard from "../components/CourseCard";

function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    setTimeout(() => {
      try {
        setCourses([
          {
            id: 1,
            name: "Python Programming",
            description: "Learn Python Basics",
            credits: 4,
          },
          {
            id: 2,
            name: "Web Development",
            description: "HTML CSS JavaScript",
            credits: 3,
          },
          {
            id: 3,
            name: "Database Systems",
            description: "Learn SQL and MySQL",
            credits: 4,
          },
        ]);
        setLoading(false);
      } catch {
        setError("Failed to load courses");
        setLoading(false);
      }
    }, 1000);
  }, []);

  function handleEnroll(course) {
    setEnrolledCourses([...enrolledCourses, course]);
    alert(course.name + " Enrolled Successfully!");
  }

  if (loading) return <h2>Loading Courses...</h2>;
  if (error) return <h2>{error}</h2>;

  return (
    <>
      <Header />

      <h2>Courses</h2>

      <p>Enrolled Courses: {enrolledCourses.length}</p>

      {courses.map((course) => (
        <CourseCard
          key={course.id}
          course={course}
          onEnroll={handleEnroll}
        />
      ))}

      <Footer />
    </>
  );
}

export default CoursesPage;