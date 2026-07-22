import { useState } from "react";

function StudentProfile() {
  const [student, setStudent] = useState({
    name: "",
    email: "",
    semester: ""
  });

  function handleChange(e) {
    setStudent({
      ...student,
      [e.target.name]: e.target.value
    });
  }

  return (
    <div>
      <h2>Student Profile</h2>

      <input
        type="text"
        name="name"
        placeholder="Name"
        value={student.name}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="email"
        name="email"
        placeholder="Email"
        value={student.email}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="text"
        name="semester"
        placeholder="Semester"
        value={student.semester}
        onChange={handleChange}
      />

      <hr />

      <h3>Preview</h3>

      <p>Name: {student.name}</p>
      <p>Email: {student.email}</p>
      <p>Semester: {student.semester}</p>
    </div>
  );
}

export default StudentProfile;