import { useContext } from "react";
import { StudentContext } from "../context/StudentContext";
import Header from "../components/Header";
import Footer from "../components/Footer";

function HomePage() {
  const { studentName } = useContext(StudentContext);

  return (
    <>
      <Header />

      <h2>Welcome {studentName}</h2>

      <p>Browse courses, enroll in subjects and manage your profile.</p>

      <Footer />
    </>
  );
}

export default HomePage;