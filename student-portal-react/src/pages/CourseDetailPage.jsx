import { useParams } from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";

function CourseDetailPage() {
  const { courseId } = useParams();

  return (
    <>
      <Header />

      <h2>Course Details</h2>

      <p>Course ID: {courseId}</p>

      <Footer />
    </>
  );
}

export default CourseDetailPage;